# AWS Project Setup Automator

Automates the repetitive manual setup required when starting a new AWS project.

## The Problem
Every new AWS project required 30+ minutes of manual work:
- Creating an S3 bucket in the AWS console
- Setting up local folder structure
- Writing configuration files from scratch

## The Solution
One Python script that does it all in under 2 minutes.

## What It Does
- Creates an S3 bucket on AWS with a unique name
- Builds local project folder structure (src, logs, config, tests)
- Uses Claude AI to generate a smart config file for the project
- Prints a full summary of everything created

## Tech Stack
- Python 3
- boto3 (AWS SDK)
- Anthropic Claude API

## How To Run

1. Clone the repo
2. Create a virtual environment and install dependencies: