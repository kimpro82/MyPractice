# Get the Total Size of Folders/Files Matching Specific Criteria
# 2024.02.29

get-childitem
echo ""
get-childitem *.ps1

get-childitem | measure-object -property length -sum
