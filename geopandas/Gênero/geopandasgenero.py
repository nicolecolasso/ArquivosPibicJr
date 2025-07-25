# -*- coding: utf-8 -*-
"""geopandasGenero.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o6E-s2lf_qqZQP5E9qCIdj1Q2k68_KGV
"""

import geopandas as gpd
import pandas as pd
import folium
from folium import Choropleth
import ipywidgets as widgets
from ipywidgets import interactive
from IPython.display import display, clear_output

br_estados = gpd.read_file("BR_UF_2024.shp")

candidatosg24 = pd.read_csv("regiaog24.csv", sep= ';', encoding= 'latin1', low_memory=False)
candidatosg12 = pd.read_csv("regiaog12.csv", sep= ';', encoding= 'latin1', low_memory=False)
candidatosg00 = pd.read_csv("regiaog00.csv", sep= ';', encoding= 'latin1', low_memory=False)
candidatosg24eleito = pd.read_csv("regiaog24eleito.csv", sep= ';', encoding= 'latin1', low_memory=False)
candidatosg12eleito = pd.read_csv("regiaog12eleito.csv", sep= ';', encoding= 'latin1', low_memory=False)
candidatosg00eleito = pd.read_csv("regiaog00eleito.csv", sep= ';', encoding= 'latin1', low_memory=False)

mulheres24 = candidatosg24[candidatosg24['Gênero'].str.contains("Feminino")]
mulheres24['Porcentagem'] = pd.to_numeric(mulheres24["Porcentagem"].astype(str).str.replace(",", ".", regex=False), errors="coerce") * 100

mulheres24eleito = candidatosg24eleito[candidatosg24eleito['Gênero'].str.contains("Feminino")]
mulheres24eleito['Porcentagem'] = pd.to_numeric(mulheres24eleito["Porcentagem"].astype(str).str.replace(",", ".", regex=False), errors="coerce") * 100

homem24 = candidatosg24[candidatosg24['Gênero'].str.contains("Masculino")]
homem24['Porcentagem'] = pd.to_numeric(homem24["Porcentagem"].astype(str).str.replace(",", ".", regex=False), errors="coerce") * 100

homem24eleito = candidatosg24eleito[candidatosg24eleito['Gênero'].str.contains("Masculino")]
homem24eleito['Porcentagem'] = pd.to_numeric(homem24eleito["Porcentagem"].astype(str).str.replace(",", ".", regex=False), errors="coerce") * 100

mulheres12 = candidatosg12[candidatosg12['Gênero'].str.contains("Feminino")]
mulheres12['Porcentagem'] = pd.to_numeric(mulheres12["Porcentagem"].astype(str).str.replace(",", ".", regex=False), errors="coerce") * 100

mulheres12eleito = candidatosg12eleito[candidatosg12eleito['Gênero'].str.contains("Feminino")]
mulheres12eleito['Porcentagem'] = pd.to_numeric(mulheres12eleito["Porcentagem"].astype(str).str.replace(",", ".", regex=False), errors="coerce") * 100

homem12 = candidatosg12[candidatosg12['Gênero'].str.contains("Masculino")]
homem12['Porcentagem'] = pd.to_numeric(homem12["Porcentagem"].astype(str).str.replace(",", ".", regex=False), errors="coerce") * 100

homem12eleito = candidatosg12eleito[candidatosg12eleito['Gênero'].str.contains("Masculino")]
homem12eleito['Porcentagem'] = pd.to_numeric(homem12eleito["Porcentagem"].astype(str).str.replace(",", ".", regex=False), errors="coerce") * 100

mulheres00 = candidatosg00[candidatosg00['Gênero'].str.contains("Feminino")]
mulheres00['Porcentagem'] = pd.to_numeric(mulheres00["Porcentagem"].astype(str).str.replace(",", ".", regex=False), errors="coerce") * 100

mulheres00eleito = candidatosg00eleito[candidatosg00eleito['Gênero'].str.contains("Feminino")]
mulheres00eleito['Porcentagem'] = pd.to_numeric(mulheres00eleito["Porcentagem"].astype(str).str.replace(",", ".", regex=False), errors="coerce") * 100

homem00 = candidatosg00[candidatosg00['Gênero'].str.contains("Masculino")]
homem00['Porcentagem'] = pd.to_numeric(homem00["Porcentagem"].astype(str).str.replace(",", ".", regex=False), errors="coerce") * 100

homem00eleito = candidatosg00eleito[candidatosg00eleito['Gênero'].str.contains("Masculino")]
homem00eleito['Porcentagem'] = pd.to_numeric(homem00eleito["Porcentagem"].astype(str).str.replace(",", ".", regex=False), errors="coerce") * 100

slider_ano = widgets.IntSlider(value=2000, min=2000, max=2024, step=12, description="Ano:")
dropdown_analise = widgets.Dropdown(options=["Masculino", "Feminino"], description="Análise:")
checkboxesEleito = widgets.Checkbox(value=False, description="Eleito")

output = widgets.Output()

def busca_func(change):
    with output:
        clear_output()
        ano = str(slider_ano.value)
        analise = dropdown_analise.value

        if ano == "2000":
            if analise == "Masculino" and checkboxesEleito.value == False:
              mapaMasculino00 = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)
              folium.Choropleth(
                  geo_data=br_estados,
                  name="choropleth",
                  data=homem00,
                  columns=["UF", "Porcentagem"],
                  key_on="feature.properties.SIGLA_UF",
                  fill_color="Oranges",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name="Candidatos masculinos por estado 2000 (%)",
              ).add_to(mapaMasculino00)
              display(mapaMasculino00)
            elif analise == "Masculino" and checkboxesEleito.value != False:
              mapaMasculino00eleito = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)
              folium.Choropleth(
                  geo_data=br_estados,
                  name="choropleth",
                  data=homem00eleito,
                  columns=["UF", "Porcentagem"],
                  key_on="feature.properties.SIGLA_UF",
                  fill_color="Oranges",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name="Candidatos masculinos por estado eleitos 2000 (%)",
              ).add_to(mapaMasculino00eleito)
              display(mapaMasculino00eleito)
            elif analise == "Feminino" and checkboxesEleito.value == False:
              mapaFeminino00 = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)
              folium.Choropleth(
                  geo_data=br_estados,
                  name="choropleth",
                  data=mulheres00,
                  columns=["UF", "Porcentagem"],
                  key_on="feature.properties.SIGLA_UF",
                  fill_color="Reds",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name="Candidatos femininos por estado 2000 (%)",
              ).add_to(mapaFeminino00)
              display(mapaFeminino00)
            elif analise == "Feminino" and checkboxesEleito.value != False:
              mapaFeminino00eleito = folium.Map(location=[-15.78897, -47.879873], zoom_start=4)
              folium.Choropleth(
                    geo_data=br_estados,
                    name="choropleth",
                    data=mulheres00eleito,
                    columns=["UF", "Porcentagem"],
                    key_on="feature.properties.SIGLA_UF",
                    fill_color="Reds",
                    fill_opacity=0.7,
                    line_opacity=0.2,
                    legend_name="Candidatos femininos por estado eleitos 2000 (%)",
              ).add_to(mapaFeminino00eleito)
              display(mapaFeminino00eleito)
        elif ano == "2012":
            if analise == "Masculino" and checkboxesEleito.value == False:
              mapaMasculino12 = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)
              folium.Choropleth(
                  geo_data=br_estados,
                  name="choropleth",
                  data=homem12,
                  columns=["UF", "Porcentagem"],
                  key_on="feature.properties.SIGLA_UF",
                  fill_color="Oranges",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name="Candidatos masculinos por estado 2012 (%)",
              ).add_to(mapaMasculino12)
              display(mapaMasculino12)
            elif analise == "Masculino" and checkboxesEleito.value != False:
              mapaMasculino12eleito = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)
              folium.Choropleth(
                  geo_data=br_estados,
                  name="choropleth",
                  data=homem12eleito,
                  columns=["UF", "Porcentagem"],
                  key_on="feature.properties.SIGLA_UF",
                  fill_color="Oranges",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name="Candidatos masculinos por estado eleitos 2012 (%)",
              ).add_to(mapaMasculino12eleito)
              display(mapaMasculino12eleito)
            elif analise == "Feminino" and checkboxesEleito.value == False:
              mapaFeminino12 = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)
              folium.Choropleth(
                  geo_data=br_estados,
                  name="choropleth",
                  data=mulheres12,
                  columns=["UF", "Porcentagem"],
                  key_on="feature.properties.SIGLA_UF",
                  fill_color="Reds",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name="Candidatos femininos por estado 2012 (%)",
              ).add_to(mapaFeminino12)
              display(mapaFeminino12)
            elif analise == "Feminino" and checkboxesEleito.value != False:
               mapaFeminino12eleito = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)
               folium.Choropleth(
                  geo_data=br_estados,
                  name="choropleth",
                  data=mulheres12eleito,
                  columns=["UF", "Porcentagem"],
                  key_on="feature.properties.SIGLA_UF",
                  fill_color="Reds",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name="Candidatos femininos por estado eleitos 2012 (%)",
               ).add_to(mapaFeminino12eleito)
               display(mapaFeminino12eleito)
        elif ano == "2024":
            if analise == "Masculino" and checkboxesEleito.value == False:
              mapaMasculino24 = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)
              folium.Choropleth(
                  geo_data=br_estados,
                  name="choropleth",
                  data=homem24,
                  columns=["UF", "Porcentagem"],
                  key_on="feature.properties.SIGLA_UF",
                  fill_color="Oranges",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name="Candidatos masculinos por estado 2024 (%)",
              ).add_to(mapaMasculino24)
              display(mapaMasculino24)
            elif analise == "Masculino" and checkboxesEleito.value != False:
               mapaMasculino24eleito = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)
               folium.Choropleth(
                  geo_data=br_estados,
                  name="choropleth",
                  data=homem24eleito,
                  columns=["UF", "Porcentagem"],
                  key_on="feature.properties.SIGLA_UF",
                  fill_color="Oranges",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name="Candidatos masculinos por estado eleitos 2024 (%)",
               ).add_to(mapaMasculino24eleito)
               display(mapaMasculino24eleito)
            elif analise == "Feminino" and checkboxesEleito.value == False:
               mapaFeminino24 = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)
               folium.Choropleth(
                  geo_data=br_estados,
                  name="choropleth",
                  data=mulheres24,
                  columns=["UF", "Porcentagem"],
                  key_on="feature.properties.SIGLA_UF",
                  fill_color="Reds",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name="Candidatos femininos por estado 2024 (%)",
              ).add_to(mapaFeminino24)
               display(mapaFeminino24)
            elif analise == "Feminino" and checkboxesEleito.value != False:
              mapaFeminino24eleito = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)
              folium.Choropleth(
                  geo_data=br_estados,
                  name="choropleth",
                  data=mulheres24eleito,
                  columns=["UF", "Porcentagem"],
                  key_on="feature.properties.SIGLA_UF",
                  fill_color="Reds",
                  fill_opacity=0.7,
                  line_opacity=0.2,
                  legend_name="Candidatos femininos por estado eleitos 2024 (%)",
              ).add_to(mapaFeminino24eleito)
              display(mapaFeminino24eleito)

slider_ano.observe(busca_func, names='value')
dropdown_analise.observe(busca_func, names='value')
checkboxesEleito.observe(busca_func, names='value')

display(slider_ano, dropdown_analise, checkboxesEleito)
display(output)

busca_func(None)