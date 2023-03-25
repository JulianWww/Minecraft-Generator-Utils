langs = {
    "af": "af_za",
    "ar": "ar_sa",
    "az": "az_az",
    "be": "be_by",
    "bg": "bg_bg",
    "bs": "bs_ba",
    "ca": "ca_es",
    "cs": "cs_cz",
    "da": "da_dk",
    "de": [
        "ast_es",
        "bar",
        "de_at",
        "de_ch",
        "de_de",
        "ksh_DE",
        "nds_de",
        "sxu",
        "ksh"
    ],
    "el": "el_gr",
    "cy": "cy_gb",
    "en": [
        "cy_bg",
        "en_au",
        "en_ca",
        "en_gb",
        "en_nz",
        "en_pt",
        "en_ud",
        "en_us",
        "enp",
        "enws",
        "kw_gb",
        "lol_us",
        "jbo_en",
        "enp",

        "fo_fo",
        "se_no",
        "tlh_aa",
        "fy_nl",
        "yo_ng",
        "qya_aa",
        "ry_ua",
        "io_en",
        "isv",
        "tl_ph",
        "tok"
    ],
    "eo": "eo_uy",
    "es": [
        "es_ar",
        "es_cl",
        "es_ec",
        "es_es",
        "es_mx",
        "es_uy",
        "es_ve",
        "esan",
        "nah",
        "val_es"
    ],
    "et": "et_ee",
    "eu": "eu_es",
    "fa": "fa_ir",
    "fi": "fi_fi",
    "fr": [
        "fr_fr",
        "br_fr",
        "fr_ca",
        "fra_de",
        "oc_fr"
    ],
    "ga": "ga_ie",
    "gd": "gl_es",
    "haw": "haw_us",
    "hi": "hi_in",
    "hr": "hr_hr",
    "hu": "hu_hu",
    "hy": "hy_am",
    "id": "id_id",
    "ig": "ig_ng",
    "is": "is_is",
    "it": [
        "it_it",
        "lmo",
        "vec_it",
        "fur_it"
    ],
    "iw": "he_il",
    "ja": "ja_jp",
    "ka": "ka_ge",
    "kk": "kk_kz",
    "kn": "kn_in",
    "ko": "ko_kr",
    "la": "la_la",
    "lb": "lb_lu",
    "lt": "lt_lt",
    "lv": "lv_lv",
    "mk": "mk_mk",
    "mn": "mn_mn",
    "ms": [
        "ms_my",
        "zlm_arab"
    ],
    "mt": "mt_mt",
    "nl": [
        "brb",
        "nl_be",
        "nl_nl",
        "li_li"
    ],
    "no": [
        "nn_no",
        "no_no"
    ],
    "pl": [
    "pl_pl",
    "szl"
    ],
    "pt": [
        "pt_br",
        "pt_pt"
    ],
    "ro": "ro_ro",
    "ru": [
        "rpr",
        "ru_ru",
        "ba_ru"
    ],
    "sk": "sk_sk",
    "sl": "sl_si",
    "so": "so_so",
    "sq": "sq_al",
    "sr": "sr_sp",
    "sv": [
        "ovd",
        "sv_se"
    ],
    "ta": "ta_in",
    "th": "th_th",
    "tl": "fil_ph",
    "tr": "tr_tr",
    "tt": "tt_ru",
    "uk": "uk_ua",
    "vi": "vi_vn",
    "yi": "yi_de",
    "yo": "ng",
    "zh-CN": [
        "lzh",
        "zh_cn",
        "zh_hk",
        "zh_tw"
    ],
    "gd": "gd_gb",
    "gl": "gl_es"
}

moveMap = {
  "nb_no": "no_no"
}

from json import load, dump
from deep_translator import GoogleTranslator
import os
from sys import argv
from time import time, sleep

langDir = f"src/main/resources/assets/{argv[1]}/lang/"
origFile = langDir + f"{argv[2]}.json"

PROXIES = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

def getMCName(trans):
  if (trans in moveMap) :
    trans = moveMap[trans]

  return trans

def getKey(trans):
  trans = getMCName(trans)
  for tkey, lang in langs.items():
    if (not isinstance(lang, list)):
      lang = [lang]
    
    for key in lang:
      if (trans.lower() == key):
        return tkey
  print(trans)


def translate(orig, dest, filename):
  with open(filename, "r") as file:
    out = load(file)

  translator = GoogleTranslator(source=argv[3], target=getKey(dest), proxies=PROXIES)
  
  for x, y in orig.items():
    while True:
      try:
        if not x in out:
          out[x] = translator.translate(y)
        break
      except Exception as e:
        sleep(0.2)

  return out

  
if __name__ == "__main__":
  with open(origFile, "r") as file:
    en_us = load(file) 

  for file in os.listdir(langDir):
    trans = file.removesuffix(".json").lower().replace("-", "_")
    out = translate(en_us, trans, langDir + file)

    os.remove(langDir + file)
    with open(langDir + getMCName(trans)+".json", "w") as file:
      dump(out, file, sort_keys=True, indent=4)
