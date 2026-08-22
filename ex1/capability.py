from abc import ABC, abstractmethod


class HealCapability(ABC):

    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class DefendCapability(ABC):
    """Something able to harden itself against incoming damage.

    Independent of Creature, like the other two. The persistent state
    lives on the concrete class and is read when damage is computed.
    """

    @abstractmethod
    def guard(self) -> str:
        pass
