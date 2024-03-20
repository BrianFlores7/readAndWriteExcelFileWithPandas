import pandas as pd
from tqdm import tqdm 

def loadExcelWithWrongRoleName() -> pd:
    df = pd.read_excel(r"C:\\Users\\AMD RYZEN 7\\Downloads\\Learn3 Permissions.xlsx")
    return df

def loadExcelWithCorrectName() -> pd:
    df = pd.read_excel(r"C:\Users\AMD RYZEN 7\Downloads\change role name (1).xlsx")
    return df

def checkRolesName(excelWithRoles):
    roles = "Capability"
    rolesList = excelWithRoles[roles]
    return rolesList

def renamePermissions(rolesName,excelWithWrongRoleName):
    limitAllPermissions = len(excelWithWrongRoleName["Permissions"]) - 1
    limitAllowedPermissions = len(rolesName)
    
    for i in tqdm(range(limitAllPermissions), desc="Checking roles"):
        allPermission = excelWithWrongRoleName.iloc[i]["Permissions"]
        for j in range(limitAllowedPermissions):      
            allowedPermission = rolesName.iloc[j]
            if allPermission == allowedPermission:
                roleName = rolesName.iloc[(j-1)]
                excelWithWrongRoleName.at[i,"Permissions"] = roleName
                
    excelWithWrongRoleName.to_excel("Correct Role Name.xlsx", sheet_name='Roles') 

if __name__ == '__main__':
    excelWithCorrectRoleName = loadExcelWithCorrectName()
    excelWithWrongRoleName = loadExcelWithWrongRoleName()
    roleName = checkRolesName(excelWithCorrectRoleName)
    renamePermissions(roleName,excelWithWrongRoleName)