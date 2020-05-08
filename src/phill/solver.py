from snek5000.info import InfoSolverMake
from snek5000.solvers.kth import SimulKTH
from phill.templates import box, size


class InfoSolverPhill(InfoSolverMake):
    """Contain the information on a :class:`eturb.solvers.abl.Simul`
    instance.

    .. todo::

        Move Output info to :class:`InfoSolverNek` and only override it in
        :class:`InfoSolverABL`.

    """

    def _init_root(self):
        super()._init_root()
        self.module_name = "phill.solver"
        self.class_name = "Simul"
        self.short_name = "phill"

        self.classes.Output.module_name = "phill.output"
        self.classes.Output.class_name = "OutputPhill"


class SimulPhill(SimulKTH):
    """A solver which compiles and runs using a Snakefile.

    """
    InfoSolver = InfoSolverPhill

    def __init__(self, params):
        super().__init__(params)
        self.output.write_box(box)
        self.output.write_size(size)


Simul = SimulPhill
