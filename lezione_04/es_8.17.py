def build_profile(primo, secondo, **informazioni):
    informazioni["primo"] = primo
    informazioni["secondo"] = secondo

    return informazioni

chiamata = build_profile("alessio", "riboldi", anni="19", capelli="biondi")
print(chiamata)
#si rispettano i standard di pep8 tramite i spazi# 
