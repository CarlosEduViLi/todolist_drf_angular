from enum import Enum, unique

@unique
class SituacaoEnum(Enum):
    ATIVA = 'Ativa'
    PAUSADA = 'Pausada'
    PENDENTE = 'Pendente'
    CONCLUIDA = 'Concluída'

    @classmethod
    def choices(cls):
        return [('','---Selecione---')] + [(tag.name, tag.value) for tag in cls]

    @classmethod
    def get_enum_value(cls, name):
        try:
            return cls[name.upper()].value
        except KeyError:
            raise ValueError(f'{name} não é uma situação válida em {cls.__name__}.')