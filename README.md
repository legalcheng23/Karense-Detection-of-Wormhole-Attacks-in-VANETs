# Enhanced Detection of Wormhole Attacks in VANETs using Karense

## Introduction

With the rapid development of intelligent transportation systems, Vehicular Ad-Hoc Networks (VANETs) have emerged as a crucial communication technology, playing an increasingly important role in enhancing traffic efficiency and road safety. VANETs enable vehicles to communicate directly with each other, facilitating information sharing and collaboration. However, as a dynamic self-organized network, VANETs face various security threats, with Wormhole Attacks being particularly serious.

A Wormhole Attack uses tunneling technology to rapidly forward data packets from one network node to a remote node. This type of attack can disrupt normal data transmission paths, cause network segmentation, data loss, and other issues, posing a significant threat to the normal operation and security of VANETs. Due to the challenging nature of detecting Wormhole Attacks, developing effective prevention strategies has become a key research focus.

## Project Purpose

This project aims to analyze the performance characteristics of Wormhole Attacks in VANETs and propose an effective defense strategy by combining multiple detection techniques. By integrating GPS-based detection, Packet Transmission Verification, and Delay per Hop Indicator (DPHI), we seek to enhance our understanding of the threats posed by Wormhole Attacks and improve detection efficiency.

## Components

1. **GPS-based Detection**: Uses geographic location data to identify abnormal communication patterns indicative of a Wormhole Attack.
2. **Packet Transmission Verification**: Validates the integrity and travel path of packets to detect malicious forwarding.
3. **Delay per Hop Indicator (DPHI)**: Measures the delay across each hop to identify unusually fast transmissions that may suggest tunneling.

## Simulation Framework

The simulation framework is based on the Ad hoc On-Demand Distance Vector (AODV) protocol. It models and analyzes various attack scenarios to verify the effectiveness of the proposed defense methods.

## Experimental Results

The experimental results demonstrate that the Karense mechanism significantly improves the detection rate of Wormhole Attacks in VANETs. On average, the detection percentage without Karense is approximately 89.5%, while with Karense, it is approximately 96.56%. These results underscore the robustness and effectiveness of Karense in mitigating the threats posed by Wormhole Attacks.

## Conclusion

The integration of GPS-based detection, Packet Transmission Verification, and DPHI in the Karense tool provides a robust defense mechanism against Wormhole Attacks, enhancing the overall security and reliability of VANETs. This study provides valuable insights and a reference for improving the security of VANETs.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/legalcheng23/Karense_Detection-of-Wormhole-Attacks-in-VANETs.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Karense_Detection-of-Wormhole-Attacks-in-VANETs
    ```

3. Run the simulation:
    ```bash
    python Karense.py
    ```

4. View the results:
    Results will be stored in the output directory as excel.

## Prerequisites

- Python 3.9.x
- Required Python libraries:
    - `numpy`
    - `matplotlib`
    - `networkx`
    - `pandas`

Install the required libraries using pip:
```bash
pip install numpy matplotlib networkx pandas
