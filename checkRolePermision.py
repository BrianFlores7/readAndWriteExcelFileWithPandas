import pandas as pd
from tqdm import tqdm 
from time import sleep 

def loadExcelWithAllowedPermission() -> pd:
    df = pd.read_excel(r"C:\Users\AMD RYZEN 7\Downloads\editingteacher.xml (1).xlsx")
    return df

def loadExcelWithAllPermission() -> pd:
    df = pd.read_excel(r"C:\\Users\\AMD RYZEN 7\\Downloads\\Learn3 Permissions.xlsx")
    return df

def checkAllowedPermissions(excelWithRoles):
    permissions = "allow"

    permissionsList = excelWithRoles[permissions]
    return permissionsList


def writeAllowedPermissions(permissionsAllowed, excelWithAllPermission):
    limitAllPermissions = len(excelWithAllPermission["Permissions"]) - 1
    limitAllowedPermissions = len(permissionsAllowed)
    
    for i in tqdm(range(limitAllowedPermissions), desc="Checking roles"):
        allowedPermission = permissionsAllowed.iloc[i]
        for j in range(limitAllPermissions):
            allPermission = excelWithAllPermission.iloc[j]["Permissions"]
            if allPermission == allowedPermission:
                excelWithAllPermission.at[i,"Manager"] = 1.0
                
    excelWithAllPermission.to_excel("Learn3 Permisions Test.xlsx", sheet_name='Roles') 

        

if __name__ == '__main__':
    excelWithAllowedPermission = loadExcelWithAllowedPermission()
    excelWithAllPermission = loadExcelWithAllPermission()
    permissionsAllowed = checkAllowedPermissions(excelWithAllowedPermission)
    writeAllowedPermissions(permissionsAllowed,excelWithAllPermission)