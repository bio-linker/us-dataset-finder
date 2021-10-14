```
~/preston-amazon$ cat zipFileNames | cut -f1 | sort | uniq -c | sort -r
     19 meta.xml
     19 eml.xml
     18 vernaculars.txt
     18 taxa.txt
     18 references.txt
     18 occurrences.txt
     18 media.txt
     18 distribution.txt
     18 description.txt
      4 multimedia.txt
      1 occurrence.txt
      1 measurementorfact.txt
andrew@DESKTOP-R1EHQ3C:~/preston-amazon$ cat zipFileNames | cut -f2 | sort | uniq -c | sort -r
     10 hash://sha256/f55bcfe2fecb108d11246b00ce3ba1a207db2b21a2f143f93e75be45299a66c1
     10 hash://sha256/6001287445869567c744d887786b5429e58cb5ef70a07b10979f0e13a14b20c7
     10 hash://sha256/2cd4e70279eca4253548a5ec32e921ec8518ec1406d4f347f90afc3caf84ce3e
     10 hash://sha256/1a8c87238e3e3a6d9721b7164ae638588eceea2e4aea411429f2f56bfd430eda
      9 hash://sha256/facc49a3bdbfc63dc755f62522efc6a3e6b60b9da37989bb0435c3ff3e5c146c
      9 hash://sha256/e1cd23814dce13e50d441ce524eaf899127f39534feea71bce95f73585ab3682
      9 hash://sha256/e0587e3526a5540c669cfbf90cd47bddec57f9e971f24dd8a36c480c3c3ec8eb
      9 hash://sha256/be5183d7122e22bfba62a5545176919451e047adbe55573e5b951132798a5f7f
      9 hash://sha256/b25f80790add77d748ec5feeabb2aaac0598b5516c12c093408d4f12b0a8eabe
      9 hash://sha256/af807efeda85b49a5707e786368b09f5a90581762ab75b53de2dbf4f4ae74686
      9 hash://sha256/a192ae333a9dffe6c25e01aa80a2f7154cd4f7bbc479f3c320faed1aa22ef2ca
      9 hash://sha256/a12376744925ced48cd50bfe2966963e7b5be9292395d841da36903e4173587c
      9 hash://sha256/94a4fc4824d951c0155860e3e5c4c662afcfae55d52a25105bca1cb6a7b3a062
      9 hash://sha256/6cea98236d8ec9c76f5f467d819f7ec363db49d6ec70985f14af912b391d918e
      9 hash://sha256/6768a340a3c820aee5db82ce377be54d1e69d036236a7e36dc27ee6bf069a009
      9 hash://sha256/5cba2f513fee9e1811fe023d54e074df2d562b4169b801f15abacd772e7528f8
      9 hash://sha256/501395573ee8f6a68a162f5a50d809686e78409aaac2c1d38d960fac6c9f2b59
      9 hash://sha256/4f81f6a14913ef7db1d45fde11b4c2e1e4e7510941606dfd645a30bda8a41d44
      4 hash://sha256/97cbeae429fbc95d1859f7afa28b33f08ac64125ba72511c49c4b77ca66d2d66
```
