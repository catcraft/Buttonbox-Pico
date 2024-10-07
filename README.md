# Buttonbox-Pico
A custom controller interface for **BeamNG**, featuring serial communication between a Raspberry Pi Pico (2) and a PC.

> **Status**: Currently under development (both software and hardware components).

## Planned Features
- **Start/Stop Engine Button**: Red/Green button specifically for controlling the engine in BeamNG.
- **Custom Buttons**: Multiple configurable buttons for various in-game actions.
- **LED Status Indicator**: Visual feedback for different status updates.
- **Controller Emulation or Keyboard Input**: Software emulation for inputs on the PC side.

## Functional Overview

### Raspberry Pi Pico (2)
- Monitors button states and controls LED colors based on status.

### PC Software
- Emulates inputs (controller/keyboard) based on signals received from the Pico.
- Integrates BeamNG **OutGauge** for real-time data communication.

### Additional Features (Future Considerations)
- **Rotary Encoder**: For enhanced input controls.
- **Display**: Shows information like gear position or RPM.

## Resources
- [BeamNG OutGauge](https://github.com/RodionGromo/outGauge_python/): A Python implementation for interfacing with BeamNG's OutGauge API.
