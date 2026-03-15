#Conditional Statements (if,elif,else)

print("Devops Deployment Environment Checker")

environment = input("Enter Deployment Environment (dev/staging/prod): ").lower()

if environment == "dev":
    print("Deploying Application in Development Environment.")
    print("Debug mode Enabled.")

elif environment == "staging":
    print("Deploying Application in Staging Environment.")
    print("Running pre-production tests.")

elif environment == "prod":
    print("Deploying Application in Production Environment.")
    print("High Security Checks Enabled.")

else:
    print("Invalid Environment Selected.")
    print("Please Choose : dev, staging or prod.")