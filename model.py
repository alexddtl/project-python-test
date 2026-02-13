import os
import logging as log

log.basicConfig(level=log.INFO)

def double(input1: int) -> int:
    return input1*input1

print(double(12))

if __name__ == "__main__":
    current_folder = os.listdir()
    log.info(f"Current folder: {current_folder}")
