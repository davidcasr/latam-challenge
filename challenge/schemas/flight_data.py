from pydantic import BaseModel, validator

class FlightData(BaseModel):
    OPERA: str
    TIPOVUELO: str
    MES: int

    @validator('TIPOVUELO')
    def check_tipo_vuelo(cls, value):
        if value not in ['I', 'N']:
            raise ValueError("TIPOVUELO must be either 'I' or 'N'.")
        return value

    @validator('MES')
    def check_mes(cls, value):
        if not (1 <= value <= 12):
            raise ValueError("MES must be between 1 and 12.")
        return value

class FlightRequest(BaseModel):
    flights: list[FlightData]