import unittest
from abc import ABC, abstractmethod
from pydantic import BaseModel
from class_property import class_property


class TestClassProperties(unittest.TestCase):
    def test_regular_implementation_and_not_implemented(self):
        class Base(ABC):
            @class_property
            @abstractmethod
            def metadata(cls) -> str:
                raise NotImplementedError

        class A(Base):
            @class_property
            def metadata(cls) -> str:
                return "a"

        class C(Base):
            pass

        self.assertEqual(A.metadata, "a")
        with self.assertRaises(NotImplementedError):
            _ = C.metadata

    def test_base_model_implementation_and_not_implemented(self):
        class Base(ABC):
            @class_property
            @abstractmethod
            def metadata(cls) -> str:
                raise NotImplementedError

        class B(Base, BaseModel):
            @class_property
            def metadata(cls) -> str:
                return "b"

        class D(Base, BaseModel):
            pass

        self.assertEqual(B.metadata, "b")
        with self.assertRaises(NotImplementedError):
            _ = D.metadata

    def test_no_exception_on_subclass_creation_without_metadata(self):
        class Base(ABC):
            @class_property
            @abstractmethod
            def metadata(cls) -> str:
                raise NotImplementedError

        class E(Base):
            pass

        try:
            _ = E()  # Attempt to instantiate E
        except Exception as e:
            self.fail(f"Instantiating E raised an exception: {e}")

    def test_incorrect_metadata_signature(self):
        with self.assertRaises(ValueError):

            class Incorrect:
                @class_property
                @abstractmethod
                def metadata(self) -> str:
                    raise NotImplementedError


if __name__ == "__main__":
    unittest.main()
