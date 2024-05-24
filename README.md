# Sign Language Translation Project

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)

## Project Overview
This project aims to develop a Sign Language Translation system using deep learning techniques. The system will leverage YOLOv5 for object detection and Torch for training and inference. The ultimate goal is to translate sign language gestures into text or spoken language, providing an accessible communication tool for the deaf and hard of hearing community.

## Technologies Used
- **PyTorch**: For building and training the neural network models.
- **YOLOv5**: For object detection, used to identify and classify sign language gestures.
- **Jenkins**: For Continuous Integration and Continuous Deployment (CI/CD).
- **AWS EC2**: For deploying the application in a scalable and reliable cloud environment.
- **Docker**: For containerizing the application to ensure consistency across different environments.

## Setup and Installation

### Prerequisites
- Python 3.8 or higher
- Git
- Docker
- AWS CLI
- Jenkins

### Clone the Repository
```sh
git clone https://github.com/yourusername/sign-language-translation.git
cd sign-language-translation
```

## Install Dependencies

Create a virtual environment and install the necessary packages:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Docker setup

Build and run the Docker container:

```sh
docker build -t sign-language-translation .
docker run -p 8000:8000 sign-language-translation
```

