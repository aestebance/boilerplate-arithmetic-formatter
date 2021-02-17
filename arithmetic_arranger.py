import re

def arithmetic_arranger(problems, result = False):
  
  dicArr = []
  returnStrings = {
    "str1": "",
    "str2": "",
    "str3": "",
    "str4": ""
  }

  if len(problems) > 5:
    return "Error: Too many problems.";
  for problem in problems:
    if '+' in problem:
      temp = []
      temp = problem.split('+');
      if len(temp) == 2:
        dicArr.append({
          "num1": temp[0],
          "operator": '+',
          "num2": temp[1]
        });
    elif '-' in problem:
      temp = []
      temp = problem.split('-');
      if len(temp) == 2:
        dicArr.append({
          "num1": temp[0],
          "operator": '-',
          "num2":temp[1]
        });
    else:
      return "Error: Operator must be '+' or '-'.";
  
  regEx = re.compile("^[0-9]+$");

  for dic in dicArr:
    dic["num1"] = dic["num1"].strip();
    if (len(dic["num1"]) > 4):
      return "Error: Numbers cannot be more than four digits.";
    else:
      dic["num1Len"] = len(dic["num1"]);
    if regEx.match(dic["num1"]):
      dic["num1"] = int(dic["num1"]);
    else:
      return "Error: Numbers must only contain digits."

    dic["num2"] = dic["num2"].strip();
    if (len(dic["num2"]) > 4):
      return "Error: Numbers cannot be more than four digits.";
    else:
      dic["num2Len"] = len(dic["num2"]);
    if regEx.match(dic["num2"]):
      dic["num2"] = int(dic["num2"]);
    else:
      return "Error: Numbers must only contain digits."

    if (dic["operator"] == "-"):
      dic["result"] = dic["num1"] - dic["num2"];
    else:
      dic["result"] = dic["num1"] + dic["num2"];
  
  for dic in dicArr:
    if (dic["num1Len"] >= dic["num2Len"]):
      returnStrings["str1"] += "  " + str(dic["num1"]) + " " * 4;
      dif = dic["num1Len"] - dic["num2Len"];
      returnStrings["str2"] += dic["operator"] + " " + " " * dif + str(dic["num2"]) + " " * 4;
      returnStrings["str3"] += "-" * int(dic["num1Len"] + 2) + " " * 4;
      if (dic["result"] < 0):
        returnStrings["str4"] += " " + " " * (dic["num1Len"] - len(str(dic["result"]))) + str(dic["result"]) + " " * 4;
      else:
        returnStrings["str4"] += "  " + " " * (dic["num1Len"] - len(str(dic["result"]))) + str(dic["result"]) + " " * 4;
    else:
      dif = dic["num2Len"] - dic["num1Len"];
      returnStrings["str1"] += " " * 2 + " " * dif + str(dic["num1"]) + " " * 4;
      returnStrings["str2"] += dic["operator"] + " " + str(dic["num2"]) + " " * 4;
      returnStrings["str3"] += "-" * int(dic["num2Len"] + 2) + " " * 4;
      if (dic["result"] < 0):
        returnStrings["str4"] += " " + " " * (dic["num2Len"] - len(str(dic["result"]))) + str(dic["result"]) + " " * 4;
      else:
        returnStrings["str4"] += "  " + " " * (dic["num2Len"] - len(str(dic["result"]))) + str(dic["result"]) + " " * 4;
  
  returnStrings["str1"] = returnStrings["str1"][:-4];
  returnStrings["str2"] = returnStrings["str2"][:-4];
  returnStrings["str3"] = returnStrings["str3"][:-4];
  returnStrings["str4"] = returnStrings["str4"][:-4];
  
  if (result):
    return returnStrings["str1"] + "\n" + returnStrings["str2"] + "\n" + returnStrings["str3"] + "\n" + returnStrings["str4"];
  else:
    return returnStrings["str1"] + "\n" + returnStrings["str2"] + "\n" + returnStrings["str3"];