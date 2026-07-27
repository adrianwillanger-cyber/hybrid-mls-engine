# Architecture

Source: `notes/system map.docx`

## System Flow

1. **Copilot Studio** (Dashboard + Workflow Orchestration)
   - Photo upload UI
   - MLS/marketing tone selector
   - MLS compliance layer
   - Narrative display panels
   - Presentation mode
   - Calls Backend API → receives JSON → renders output

2. **Azure API** (Azure Functions / App Service) — `Backend/`
   - Runs the task engine
   - Processes photos
   - Runs feature detection
   - Applies MLS compliance filters
   - Generates narratives
   - Returns JSON to Copilot Studio

3. **Azure Blob Storage**
   - Stores uploaded photos
   - Stores compliance logs
   - Stores versioned outputs
   - Stores market CSV files

4. **GitHub**
   - Stores backend code
   - Stores JSON schemas (`Schema/`)
   - Stores branding theme (`Branding/`)
   - Stores MLS compliance rules
   - Stores feature detection logic
   - CI/CD pipeline → deploys to Azure (`.github/workflows/deploy_to_azure.yml`)
