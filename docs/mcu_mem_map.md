## Flash
| Start address | End address | Description                   |
| --            |  --         | --                            |
| `0x00000`     | `0x0EFFF`   | Normal operation mode program |
| `0x0F000`     | `0x0FFFF`   | Firmware update mode program  |
| `0x10000`     | `0x107FF`   | Boot code                     |


## RAM 
RAM memory mapped at address `0x20000000`

## Peripherals 

| Address      | Description                   |
| --           | --                            |
| `0x4006B800` | Uart base address             |
| `0x40060000` | GPIO - PORT0 base address     |
| `0x40061000` | GPIO - PORT1 base address     |
