import uctypes

"""
Documentation: https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf

"""

RNG_DATA_REG = 0x3ff75144   # random number data
RNG_DATA_BYTES = 4          # 32 bit random number

def get_hardware_rng():
    """
    Return a 32-bit harware generated random number. According to
    documentation
    """
    return uctypes.bytes_at(RNG_DATA_REG, RNG_DATA_BYTES) 


