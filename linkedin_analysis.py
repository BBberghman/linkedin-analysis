# -*- coding: utf-8 -*-
"""
Based on: https://github.com/tavishcode/linkedin_analysis
"""

import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv('CSV_Connections.csv')
df = df.dropna(subset=['Company'])

# modify date and add column for year and month connected on
df['Connected On'] = pd.to_datetime(df['Connected On'], format="%d %b %Y")
df['Year Connected On'] = df['Connected On'].dt.year
df['Month Connected On'] = df['Connected On'].dt.month

# create root node for treemap
df['My Network'] = 'My Network'

# group company synonyms
company=df['Company']
ulb = company.str.contains('Ecole Polytechnique de Bruxelles|Brussels School of Engineering|BEP|IRIDIA|A.Ir.Br|Université libre de Bruxelles|ULB|HeLSci|Solvay Student Consulting Club|Cercle Solvay|SBS-EM|Solvay Digital Society',
                       case=False) & ~company.str.contains('ULB Coopération|ULB-Coopération', case=False)
ulbco = company.str.contains('ULB Coopération|ULB-Coopération', case=False)
un = company.str.contains('United Nations|MONUSCO|Nations unies', case=False)
who = company.str.contains('WHO|OMS|Organisation mondiale de la Santé|World Health Organization', case=False)
aedes = company.str.contains('AEDES|Agence européenne pour le développement et la santé', case=False)
hpnk = company.str.contains('Hôpital provincial du Nord-kivu|Provincial Hospital of the North-Kivu', case=False)
louvainco=company.str.contains('Louvain Coopération', case=False)
eclosio=company.str.contains('Eclosio', case=False)
engie = company.str.contains('ENGIE', case=False)
mcKinsey = company.str.contains('McKinsey', case=False)
belgiumImpl = company.str.contains('Belgium', case=False)

couples = [(ulb, 'Université libre de Bruxelles'),
         (ulbco, 'ULB-Coopération'),
         (un, 'United Nations'),
         (who, 'WHO'),
         (aedes, 'AEDES'),
         (hpnk, 'HPNK'),
         (louvainco, 'Louvain Coopération'),
         (eclosio, 'Eclosio'),
         (engie, 'ENGIE'),
         (mcKinsey, 'McKinsey & Company'),
         (belgiumImpl, df['Company'].str.replace('Belgium','',case=False))]

for tuple in couples:
    df['Company']=np.where(tuple[0], tuple[1], df['Company'])


#treemap of Company
fig1 = px.treemap(df,
                  path=['My Network', 'Company', 'Position'],
                  width=1000,
                  height=1000)
fig1.show()

#treemap of firstname
fig2 = px.treemap(df,
                  path=['My Network', 'First Name', 'Company'],
                  width=1000,
                  height=1000)
fig2.show()

#treemap of current name of company given when I connected with them
fig3 = px.treemap(df,
                  path=['My Network', 'Year Connected On', 'Company'],
                  width=1000,
                  height=1000,
                  color='Company',
                  color_discrete_sequence=px.colors.qualitative.Set3)
fig3.show()