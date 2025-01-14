# -*- coding: utf-8 -*-

import brainpy as bp
from brainpy.dyn import neurons, synapses


class HippoThaCortexModel(bp.dyn.Network):
  def __init__(self, ):
    super(HippoThaCortexModel, self).__init__()

    self.CA1Exc = neurons.AdExIF(800, R=1/7., tau=200/7., V_rest=-58, delta_T=2.,
                                 V_T=-50, tau_w=120, a=2, V_th=0., V_reset=-46, b=100)
    self.CA3Exc = neurons.AdExIF(1200, R=1/7., tau=200/7., V_rest=-58, delta_T=2.,
                                 V_T=-50, tau_w=120, a=2, V_th=0., V_reset=-46, b=40)
    self.CA1Inh = neurons.AdExIF(160, R=1/10., tau=200/10., V_rest=-70, delta_T=2.,
                                 V_T=-50, tau_w=30, a=2, V_th=0., V_reset=-58, b=10)
    self.CA3Inh = neurons.AdExIF(240, R=1/10., tau=200/10., V_rest=-70, delta_T=2.,
                                 V_T=-50, tau_w=30, a=2, V_th=0., V_reset=-58, b=10)
    for pop in [self.CA1Exc, self.CA3Exc, self.CA1Inh, self.CA3Inh]:
      ou = neurons.OUProcess(self.CA1Exc.size, )
      conn = synapses.WeightedSum(ou, pop, bp.conn.One2One())
      self.register_implicit_nodes(ou, conn)




