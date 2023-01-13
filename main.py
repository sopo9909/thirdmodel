import os
import shutil


def to_do_logic(param_json: dict, in_dir: str, out_dir: str):
    hoyoung = param_json.get("hoyoung", None)
    tom = param_json.get("tom", None)
    anything = param_json.get("anything", None)
    nonvalue = param_json.get("nonvalue", None)
    output: dict = {
        "hoyoung": f"{hoyoung} third",
        "tom": f"{tom} third",
        "anything": f"{anything} third",
    }
    return output


# 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

if __name__ == "__main__":
    param_json = {
        "hoyoung": "only work s laves",
        "tom": "God",
        "anything": "nothing has changed",
    }
    to_do_logic(param_json, f"{os.getcwd()}{os.sep}hodir", f"{os.getcwd()}{os.sep}hooutdir")
