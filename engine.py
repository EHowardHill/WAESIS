import face_recognition
import os
import pickle
from pathlib import Path

data = [{ "label": 'Wjatkid', "value": 'Volgid'}, 
{ "label": 'Adriatic', "value": 'Dinarid'}, 
{ "label": 'Adriatic', "value": 'basic/Dinarid'}, 
{ "label": 'Aegyptid', "value": 'Egyptid'}, 
{ "label": 'Aetid', "value": 'Aetid'}, 
{ "label": 'African Alpine', "value": 'AfricanAlpinoid'}, 
{ "label": 'African Alpinoid ', "value": 'AfricanAlpinoid'}, 
{ "label": 'African Negrito', "value": 'basic/Bambutid'}, 
{ "label": 'Aino', "value": 'Aoshima'}, 
{ "label": 'Ainoid', "value": 'Aoshima'}, 
{ "label": 'Ainoid', "value": 'basic/Ainuid'}, 
{ "label": 'Ainoida', "value": 'basic/Ainuid'}, 
{ "label": 'Aïnou', "value": 'Aoshima'}, 
{ "label": 'Ainu', "value": 'Aoshima'}, 
{ "label": 'Ainuid', "value": 'basic/Ainuid'}, 
{ "label": 'Aisto Nordid', "value": 'AistoNordid'}, 
{ "label": 'Alaskan Eskimo', "value": 'BeringSea'}, 
{ "label": 'Aleutìna', "value": 'basic/Pacifid'}, 
{ "label": 'Alföld', "value": 'Alfoeld'}, 
{ "label": 'Alkonkinid ', "value": 'Appalacid'}, 
{ "label": 'Alkonkinid ', "value": 'Appalacid'}, 
{ "label": 'Alleganica', "value": 'Appalacid'}, 
{ "label": 'Alpin', "value": 'basic/Alpinid'}, 
{ "label": 'Alpina', "value": 'basic/Alpinid'}, 
{ "label": 'Alpine', "value": 'basic/Alpinid'}, 
{ "label": 'Alpinid', "value": 'basic/Alpinid'}, 
{ "label": 'Altai-Caspian', "value": 'Aralid'}, 
{ "label": 'Altnordid', "value": 'ProtoNordid'}, 
{ "label": 'Amazonian', "value": 'basic/Amazonid'}, 
{ "label": 'Amazonid', "value": 'basic/Amazonid'}, 
{ "label": 'Amérindienne des Pampas', "value": 'basic/Patagonid'}, 
{ "label": 'Amur-Sakhalin', "value": 'AmurSakhalin'}, 
{ "label": 'Anatolid', "value": 'Anatolid'}, 
{ "label": 'Anatolienne', "value": 'basic/Armenoid'}, 
{ "label": 'Andamanid', "value": 'NorthAndamanid'}, 
{ "label": 'Andean', "value": 'basic/Andid'}, 
{ "label": 'Andid', "value": 'basic/Andid'}, 
{ "label": 'Andronovo-Turanid', "value": 'AndronovoTuranid'}, 
{ "label": 'Anglo-Saxon', "value": 'AngloSaxon'}, 
{ "label": 'Annamid', "value": 'Annamid'}, 
{ "label": 'Aoshima', "value": 'Aoshima'}, 
{ "label": 'Arabe', "value": 'basic/Orientalid'}, 
{ "label": 'Arabian Veddoid ', "value": 'ArabianVeddoid'}, 
{ "label": 'Arabid', "value": 'Arabid'}, 
{ "label": 'Araboid', "value": 'Arabid'}, 
{ "label": 'Arabo-Mediterranean', "value": 'Arabid'}, 
{ "label": 'Aralid', "value": 'Aralid'}, 
{ "label": 'Arin Nordid', "value": 'ProtoNordid'}, 
{ "label": 'Arizonid', "value": 'Arizonid'}, 
{ "label": 'Armenid ', "value": 'Armenid'}, 
{ "label": 'Armenoid', "value": 'basic/Armenoid'}, 
{ "label": 'Artic', "value": 'basic/Eskimid '}, 
{ "label": 'Ashiwid', "value": 'Pueblid '}, 
{ "label": 'Asiatic Alpine', "value": 'EastAlpinid'}, 
{ "label": 'Assurid ', "value": 'Assyroid'}, 
{ "label": 'Assyroid', "value": 'Assyroid'}, 
{ "label": 'Atanto Mediterranid', "value": 'Eurafricanid'}, 
{ "label": 'Athabaskid', "value": 'Athabaskid'}, 
{ "label": 'Äthiopid', "value": 'basic/Ethiopid'}, 
{ "label": 'Atlantic', "value": 'basic/Silvid'}, 
{ "label": 'Atlantid', "value": 'NorthAtlantid'}, 
{ "label": 'Atlanto-Baltic', "value": 'basic/Nordid'}, 
{ "label": 'Australian', "value": 'basic/Australid'}, 
{ "label": 'Australian Aborigines', "value": 'basic/Australid'}, 
{ "label": 'Australid', "value": 'basic/Australid'}, 
{ "label": 'Australoid Semang', "value": 'JahaiSemangid'}, 
{ "label": 'Australo-Pygmid', "value": 'Barrinean'}, 
{ "label": 'Ba Twa', "value": 'TwaCwa'}, 
{ "label": 'BaBinga', "value": 'WestBambutid'}, 
{ "label": 'Baltic', "value": 'basic/EastEuropid'}, 
{ "label": 'BaMbuti', "value": 'EastBambutid'}, 
{ "label": 'Bambutid', "value": 'basic/Bambutid'}, 
{ "label": 'Bantu', "value": 'basic/Bantuid'}, 
{ "label": 'Bantuid', "value": 'basic/Bantuid'}, 
{ "label": 'Barrinean', "value": 'Barrinean'}, 
{ "label": 'Baskid  ', "value": 'Baskid'}, 
{ "label": 'Baykal ', "value": 'Baykal'}, 
{ "label": 'Berberid', "value": 'Berberid'}, 
{ "label": 'Bergdama', "value": 'MountainDama'}, 
{ "label": 'Berid', "value": 'Berberid'}, 
{ "label": 'Paleo Mediterranean', "value": 'PaleoSardinian'}, 
{ "label": 'Bering Sea', "value": 'BeringSea'}, 
{ "label": 'Bhaca-Swazi-Zulu', "value": 'SouthBantuid'}, 
{ "label": 'Birmana', "value": 'Shanid'}, 
{ "label": 'Black Breed', "value": 'PaleoAtlantid'}, 
{ "label": 'Bobo', "value": 'Bobo'}, 
{ "label": 'Bororo', "value": 'Bororo'}, 
{ "label": 'Borreby', "value": 'Borreby'}, 
{ "label": 'Boscimana', "value": 'basic/Sanid'}, 
{ "label": 'Botocudo', "value": 'Botocudo'}, 
{ "label": 'Brachio Melanesid', "value": 'BrachioMelanesid'}, 
{ "label": 'Brachio Melanesid    ', "value": 'BrachioMelanesid'}, 
{ "label": 'Brasilid', "value": 'basic/Amazonid'}, 
{ "label": 'Britannico', "value": 'AngloSaxon'}, 
{ "label": 'Brünn', "value": 'PaleoAtlantid'}, 
{ "label": 'Buka', "value": 'Bukaid'}, 
{ "label": 'Bukaid', "value": 'Bukaid'}, 
{ "label": 'Buryat-Kalmyk ', "value": 'Gobid'}, 
{ "label": 'Bushman', "value": 'basic/Sanid'}, 
{ "label": 'Cafra', "value": 'basic/Bantuid'}, 
{ "label": 'California Pacifid', "value": 'CaliforniaPacifid'}, 
{ "label": 'Californian', "value": 'CaliforniaPacifid'}, 
{ "label": 'Californian (Sonorid)', "value": 'Californid'}, 
{ "label": 'Californid', "value": 'Californid'}, 
{ "label": 'Camerroonian', "value": 'WestCongolesid'}, 
{ "label": 'Campid', "value": 'LagoaSanta'}, 
{ "label": 'Canarese', "value": 'Malabarese'}, 
{ "label": 'Canarid', "value": 'Canarid'}, 
{ "label": 'Cappadocian', "value": 'Arabid'}, 
{ "label": 'Carolinese', "value": 'Micronesid'}, 
{ "label": 'Carpathian', "value": 'Carpathid'}, 
{ "label": 'Carpathid ', "value": 'Carpathid'}, 
{ "label": 'Carpatico', "value": 'Gorid'}, 
{ "label": 'Carpatico', "value": 'Gorid'}, 
{ "label": 'Carpentarian', "value": 'NorthAustralid'}, 
{ "label": 'Carpentarid', "value": 'NorthAustralid'}, 
{ "label": 'Casamance', "value": 'Casamance'}, 
{ "label": 'Caspian', "value": 'Iranid'}, 
{ "label": 'Caucasid', "value": 'Mtebid'}, 
{ "label": 'Central African', "value": 'basic/Bambutid'}, 
{ "label": 'Central American', "value": 'basic/Centralid'}, 
{ "label": 'Central Andid', "value": 'CentralAndid'}, 
{ "label": 'Central Asiatic', "value": 'Gobid'}, 
{ "label": 'Central Bambutid', "value": 'TwaCwa'}, 
{ "label": 'Central Bantuid', "value": 'CentralBantuid'}, 
{ "label": 'Central Brachid ', "value": 'CentralBrachid'}, 
{ "label": 'Central Eastern European', "value": 'NorthPontid'}, 
{ "label": 'Central Ethiopid', "value": 'CentralEthiopid'}, 
{ "label": 'Central Gondid', "value": 'SouthGondid'}, 
{ "label": 'Central Negrillo', "value": 'TwaCwa'}, 
{ "label": 'Central Pamirid', "value": 'CentralPamirid'}, 
{ "label": 'Central-Asiatic-Inter-River', "value": 'Turanid'}, 
{ "label": 'Centralid', "value": 'basic/Centralid'}, 
{ "label": 'Cevennid', "value": 'WestAlpinid'}, 
{ "label": 'Changkiangid', "value": 'Changkiangid'}, 
{ "label": 'Columbica', "value": 'basic/Andid'}, 
{ "label": 'Columbid', "value": 'basic/Pacifid'}, 
{ "label": 'Congolaise', "value": 'Congolesid'}, 
{ "label": 'Congolesid', "value": 'Congolesid'}, 
{ "label": 'Congolid', "value": 'basic/Congolid'}, 
{ "label": 'Coptic', "value": 'Egyptid'}, 
{ "label": 'Costiera', "value": 'Strandlooper'}, 
{ "label": 'Dakota', "value": 'Planid'}, 
{ "label": 'Dalic', "value": 'Dalofaelid'}, 
{ "label": 'Dalo Nordid ', "value": 'Dalofaelid'}, 
{ "label": 'Dalofaelid', "value": 'Dalofaelid'}, 
{ "label": 'Dalofalid', "value": 'Dalofaelid'}, 
{ "label": 'Danakil', "value": 'Danakil'}, 
{ "label": 'Danube-March', "value": 'PreSlavic'}, 
{ "label": 'Dardic', "value": 'IndoNordic'}, 
{ "label": 'Dayakid', "value": 'Dayakid'}, 
{ "label": 'Deneid', "value": 'basic/Pacifid'}, 
{ "label": 'Desert Australid', "value": 'DesertAustralid'}, 
{ "label": 'Deutero Malayid', "value": 'DeuteroMalayid'}, 
{ "label": 'Dinaric', "value": 'basic/Dinarid'}, 
{ "label": 'Dinaricized Mediterranid', "value": 'Litorid'}, 
{ "label": 'Dinarid', "value": 'Dinarid'}, 
{ "label": 'Dnieper-Carphatian', "value": 'Carpathid'}, 
{ "label": 'Dravidian', "value": 'basic/IndoMelanid'}, 
{ "label": 'Early Egyptian', "value": 'Egyptid'}, 
{ "label": 'East African', "value": 'basic/Ethiopid'}, 
{ "label": 'East Alpinid', "value": 'EastAlpinid'}, 
{ "label": 'East Baltic', "value": 'Tavastid'}, 
{ "label": 'East Baltid', "value": 'Tavastid'}, 
{ "label": 'East Bambutid', "value": 'EastBambutid'}, 
{ "label": 'East Bantuid', "value": 'NorthBantuid'}, 
{ "label": 'East Brachid', "value": 'EastBrachid'}, 
{ "label": 'East Ethiopid', "value": 'EastEthiopid'}, 
{ "label": 'East European', "value": 'basic/EastEuropid'}, 
{ "label": 'East Europid', "value": 'basic/EastEuropid'}, 
{ "label": 'East Negrillo', "value": 'basic/EastBambutid'}, 
{ "label": 'East Nordid', "value": 'ProtoNordid'}, 
{ "label": 'East Nordid', "value": 'ProtoNordid'}, 
{ "label": 'East Palaungid', "value": 'EastPalaungid'}, 
{ "label": 'East Pamirid', "value": 'EastPamirid'}, 
{ "label": 'East Shanid', "value": 'EastShanid'}, 
{ "label": 'East Sudanid', "value": 'EastSudanid'}, 
{ "label": 'Eastern', "value": 'NeoDanubian'}, 
{ "label": 'Eastern Baltic', "value": 'basic/EastEuropid'}, 
{ "label": 'EastVeddid', "value": 'Senoid'}, 
{ "label": 'Egyptid', "value": 'Egyptid'}, 
{ "label": 'Equatorial Sudanid', "value": 'EquatorialSudanid'}, 
{ "label": 'Eschimidi', "value": 'basic/Eskimid '}, 
{ "label": 'Eskimid ', "value": 'basic/Eskimid '}, 
{ "label": 'Esqímidos', "value": 'basic/Eskimid '}, 
{ "label": 'Est-Européenne', "value": 'basic/EastEuropid'}, 
{ "label": 'Estonian West Baltic', "value": 'AistoNordid'}, 
{ "label": 'Ethiopian', "value": 'basic/Ethiopid'}, 
{ "label": 'Eurafricanid', "value": 'Eurafricanid'}, 
{ "label": 'Eurasian steppe type', "value": 'AndronovoTuranid'}, 
{ "label": 'Faelid', "value": 'Dalofaelid'}, 
{ "label": 'Fälo Nordid', "value": 'Dalofaelid'}, 
{ "label": 'Fang', "value": 'EquatorialSudanid'}, 
{ "label": 'Fengu-Pondo', "value": 'FenguPondo'}, 
{ "label": 'Fenno Nordid', "value": 'FennoNordid'}, 
{ "label": 'Fezzan', "value": 'Fezzanid'}, 
{ "label": 'Fezzanid', "value": 'Fezzanid'}, 
{ "label": 'Fijian', "value": 'Fijid'}, 
{ "label": 'Fijid', "value": 'Fijid'}, 
{ "label": 'Fingo-Hlubi-Mpondo', "value": 'FenguPondo'}, 
{ "label": 'Finnic', "value": 'FennoNordid'}, 
{ "label": 'Forest Negro', "value": 'basic/Congolid'}, 
{ "label": 'Fuegid', "value": 'SouthFuegid'}, 
{ "label": 'Gangid', "value": 'GracileIndid'}, 
{ "label": 'Garwahli', "value": 'MountainIndid'}, 
{ "label": 'Georgiana', "value": 'Mtebid'}, 
{ "label": 'Gerba', "value": 'AfricanAlpinoid'}, 
{ "label": 'Gobid', "value": 'Gobid'}, 
{ "label": 'Gondid', "value": 'North Gondid'}, 
{ "label": 'Gorid', "value": 'Gorid'}, 
{ "label": 'Göta', "value": 'Hallstatt'}, 
{ "label": 'Gracile Gondid', "value": 'SouthGondid'}, 
{ "label": 'Gracile Indid', "value": 'GracileIndid'}, 
{ "label": 'Gracile Mediterranid', "value": 'GracileMediterranid'}, 
{ "label": 'Gracile Polinesian', "value": 'Nesiotid'}, 
{ "label": 'Grazilmediterranid', "value": 'GracileMediterranid'}, 
{ "label": 'Guanche', "value": 'Canarid'}, 
{ "label": 'Guinéenne-Congolaise', "value": 'basic/Congolid'}, 
{ "label": 'Guineo Camerunian', "value": 'GuineoCamerunian'}, 
{ "label": 'Guinéo-Camerounais', "value": 'GuineoCamerunian'}, 
{ "label": 'Guinesid', "value": 'Guinesid'}, 
{ "label": 'Hadza', "value": 'Hadza'}, 
{ "label": 'Hallstatt', "value": 'Hallstatt'}, 
{ "label": 'Hamite', "value": 'basic/Ethiopid'}, 
{ "label": 'Hebraic', "value": 'Assyroid'}, 
{ "label": 'Highland type', "value": 'Kham'}, 
{ "label": 'Himalaya', "value": 'MountainIndid'}, 
{ "label": 'Himalayan', "value": 'Tibetid'}, 
{ "label": 'Himyaritic', "value": 'Yemenid'}, 
{ "label": 'Hoid', "value": 'Huanghoid'}, 
{ "label": 'Homo africanus', "value": 'basic/Ethiopid'}, 
{ "label": 'Homo akkalis', "value": 'basic/Bambutid'}, 
{ "label": 'Homo alpinus', "value": 'basic/Alpinid'}, 
{ "label": 'Homo Australasicus', "value": 'basic/Australid'}, 
{ "label": 'Homo curilanus', "value": 'basic/Ainuid'}, 
{ "label": 'Homo Dinaricus', "value": 'basic/Dinarid'}, 
{ "label": 'Homo groenlandus', "value": 'basic/Eskimid '}, 
{ "label": 'Homo hottentottus', "value": 'Khoid'}, 
{ "label": 'Homo indicus', "value": 'basic/Indid'}, 
{ "label": 'Homo indicus brachimorphus', "value": 'IndoBrachid '}, 
{ "label": 'Homo lappo', "value": 'basic/Lappid'}, 
{ "label": 'Homo melanicus', "value": 'basic/Melanesid'}, 
{ "label": 'Homo mongoloideus', "value": 'basic/Sibirid'}, 
{ "label": 'Homo negrito', "value": 'basic/Negritid'}, 
{ "label": 'Homo patagonicus', "value": 'basic/Patagonid'}, 
{ "label": 'Homo slavonicus', "value": 'basic/EastEuropid'}, 
{ "label": 'Homo sudanensis', "value": 'Sudanid'}, 
{ "label": 'Homo syriacus', "value": 'basic/Armenoid'}, 
{ "label": 'Hottentot', "value": 'Khoid'}, 
{ "label": 'Huanghoid', "value": 'Huanghoid'}, 
{ "label": 'Huarpid', "value": 'Huarpid'}, 
{ "label": 'Hylänegrid', "value": 'basic/Congolid'}, 
{ "label": 'Hyläid', "value": 'basic/Congolid'}, 
{ "label": 'Ibero Insular', "value": 'GracileMediterranid'}, 
{ "label": 'Indid', "value": 'basic/Indid'}, 
{ "label": 'Indo Brachid', "value": 'IndoBrachid'}, 
{ "label": 'Indo Iranid', "value": 'IndoIranid'}, 
{ "label": 'Indo Iranus', "value": 'IndoIranid'}, 
{ "label": 'Indo Melanid', "value": 'basic/IndoMelanid'}, 
{ "label": 'Indo Nordic', "value": 'IndoNordic'}, 
{ "label": 'Indo-Afghan', "value": 'NorthIndid'}, 
{ "label": 'Indo-Afghan', "value": 'basic/Indid'}, 
{ "label": 'Indo-Aryan', "value": 'NorthIndid'}, 
{ "label": 'Indo-Dravidian', "value": 'GracileIndid'}, 
{ "label": 'Indo-Dravidian', "value": 'basic/Indid'}, 
{ "label": 'Indomelanid', "value": 'basic/IndoMelanid'}, 
{ "label": 'Indonesian ', "value": 'Dayakid'}, 
{ "label": 'Indo-Scythian', "value": 'GracileIndid'}, 
{ "label": 'Inland Fuegid', "value": 'Huarpid'}, 
{ "label": 'Insular Melanesid', "value": 'InsularMelanesid'}, 
{ "label": 'Inuid', "value": 'Inuid'}, 
{ "label": 'Iranian Nordoid', "value": 'ProtoNordid'}, 
{ "label": 'Iraniana', "value": 'basic/Orientalid'}, 
{ "label": 'Iranid', "value": 'Iranid'}, 
{ "label": 'Irish ', "value": 'NorthAtlantid'}, 
{ "label": 'Ishikawa', "value": 'Ishikawa'}, 
{ "label": 'Isthmid', "value": 'Isthmid'}, 
{ "label": 'Iswanid', "value": 'Pueblid '}, 
{ "label": 'Jahai', "value": 'JahaiSemangid'}, 
{ "label": 'Jahai Semangid', "value": 'JahaiSemangid'}, 
{ "label": 'Kachinid', "value": 'Kachinid'}, 
{ "label": 'Kackid', "value": 'NorthLappid'}, 
{ "label": 'Kafrid', "value": 'basic/Bantuid'}, 
{ "label": 'Kalaharid', "value": 'Kalaharid'}, 
{ "label": 'Kambodischid', "value": 'Khmerid'}, 
{ "label": 'Karnatid', "value": 'Karnatid'}, 
{ "label": 'Karroid', "value": 'Karroid'}, 
{ "label": 'Katanga', "value": 'Katanga'}, 
{ "label": 'Katangid', "value": 'Katangid'}, 
{ "label": 'Keltic', "value": 'NorthAtlantid'}, 
{ "label": 'Keltoid', "value": 'basic/Alpinid'}, 
{ "label": 'Kensieu', "value": 'Semangid'}, 
{ "label": 'Keralid', "value": 'Keralid'}, 
{ "label": 'Kham', "value": 'Kham'}, 
{ "label": 'Khmerid', "value": 'Khmerid'}, 
{ "label": 'Khoid', "value": 'Khoid'}, 
{ "label": 'Khoinid', "value": 'Khoid'}, 
{ "label": 'Khurasan', "value": 'Iranid'}, 
{ "label": 'Kiangid', "value": 'basic/Changkiangid'}, 
{ "label": 'Kolarid ', "value": 'Kolid'}, 
{ "label": 'Kolid', "value": 'Kolid'}, 
{ "label": 'Kongoid', "value": 'basic/Congolid'}, 
{ "label": 'Korean', "value": 'ManchuKorean'}, 
{ "label": 'Kourilienne', "value": 'basic/Ainuid'}, 
{ "label": 'Kthela', "value": 'Gorid'}, 
{ "label": 'Kumid', "value": 'Aralid'}, 
{ "label": 'Kurgan', "value": 'Pontid'}, 
{ "label": 'Kurilian', "value": 'basic/Ainuid'}, 
{ "label": 'Ladogan', "value": 'Ladogan'}, 
{ "label": 'Lagid', "value": 'basic/Lagid'}, 
{ "label": 'Lagoa Santa', "value": 'LagoaSanta'}, 
{ "label": 'Lagoana', "value": 'LagoaSanta'}, 
{ "label": 'Lakotid', "value": 'Planid'}, 
{ "label": 'Laponoid', "value": 'basic/Lappid'}, 
{ "label": 'Lapp', "value": 'basic/Lappid'}, 
{ "label": 'Lappid', "value": 'basic/Lappid'}, 
{ "label": 'Lappon', "value": 'basic/Lappid'}, 
{ "label": 'Lenapid ', "value": 'Appalacid'}, 
{ "label": 'Libyid', "value": 'Libyid'}, 
{ "label": 'Libyid', "value": 'Libyid'}, 
{ "label": 'Litorid', "value": 'Litorid'}, 
{ "label": 'Litorid   ', "value": 'Litorid'}, 
{ "label": 'Litoroid', "value": 'Litorid'}, 
{ "label": 'Littoral', "value": 'Litorid'}, 
{ "label": 'Lower Dnieper ', "value": 'Carpathid'}, 
{ "label": 'Maasai', "value": 'Maasai'}, 
{ "label": 'Magellanid', "value": 'SouthFuegid'}, 
{ "label": 'Malabarese', "value": 'Malabarese'}, 
{ "label": 'Malagasid', "value": 'Malagasid'}, 
{ "label": 'Malaid', "value": 'DeuteroMalayid'}, 
{ "label": 'Malay', "value": 'DeuteroMalayid'}, 
{ "label": 'Malay-Mongolid', "value": 'DeuteroMalayid'}, 
{ "label": 'Malgascia', "value": 'Malagasid'}, 
{ "label": 'Malid', "value": 'Malid'}, 
{ "label": 'Manchu-Korean', "value": 'ManchuKorean'}, 
{ "label": 'Maori-Pasquese', "value": 'SouthPolynesid'}, 
{ "label": 'Margid', "value": 'basic/Margid'}, 
{ "label": 'Margoid Centralid', "value": 'Maya'}, 
{ "label": 'Maritime Tungid', "value": 'AmurSakhalin'}, 
{ "label": 'Maya', "value": 'Maya'}, 
{ "label": 'Mediterranean Indian', "value": 'basic/Indid'}, 
{ "label": 'Melanesian', "value": 'basic/Melanesid'}, 
{ "label": 'Melanesian-Papuan', "value": 'basic/Melanesid'}, 
{ "label": 'Melanesid', "value": 'basic/Melanesid'}, 
{ "label": 'Mélanésienne', "value": 'basic/Melanesid'}, 
{ "label": 'Melanid', "value": 'Karnatid'}, 
{ "label": 'Mélano-Indienne', "value": 'basic/IndoMelanid'}, 
{ "label": 'Mexicid', "value": 'Mexicid'}, 
{ "label": 'Micronesid', "value": 'Micronesid'}, 
{ "label": 'Middle Nile', "value": 'MiddleNile'}, 
{ "label": 'Middle Sinid', "value": 'Changkiangid'}, 
{ "label": 'Miyato island dwarf', "value": 'Ishikawa'}, 
{ "label": 'Moorish', "value": 'Moorish'}, 
{ "label": 'Mountain Aralid', "value": 'MountainAralid'}, 
{ "label": 'Mountain Cave', "value": 'LagoaSanta'}, 
{ "label": 'Mountain Dama', "value": 'MountainDama'}, 
{ "label": 'Mountain Indid', "value": 'MountainIndid'}, 
{ "label": 'Mountain Melanesid', "value": 'MountainMelanesid'}, 
{ "label": 'Mountain Pamirid ', "value": 'CentralPamirid'}, 
{ "label": 'Mountain Papua', "value": 'MountainMelanesid'}, 
{ "label": 'Mtebid', "value": 'Mtebid'}, 
{ "label": 'Mundari', "value": 'Kolid'}, 
{ "label": 'Mundu Mangbeto', "value": 'MunduMangbeto'}, 
{ "label": 'Murraian', "value": 'SouthAustralid'}, 
{ "label": 'Murray', "value": 'SouthAustralid'}, 
{ "label": 'Murrayian', "value": 'SouthAustralid'}, 
{ "label": 'Murrayid', "value": 'SouthAustralid'}, 
{ "label": 'Nagid', "value": 'Kachinid'}, 
{ "label": 'Near Asiatic', "value": 'basic/Armenoid'}, 
{ "label": 'Near Eastern', "value": 'Armenid'}, 
{ "label": 'Nègre Paléotropicale', "value": 'basic/Congolid'}, 
{ "label": 'Negrillo', "value": 'basic/Bambutid'}, 
{ "label": 'Negritid', "value": 'basic/Negritid'}, 
{ "label": 'Negritid', "value": 'basic/Negritid'}, 
{ "label": 'Negrito', "value": 'basic/Negritid'}, 
{ "label": 'Negrito Philippine', "value": 'Aetid'}, 
{ "label": 'Neo Danubian', "value": 'NeoDanubian'}, 
{ "label": 'Neo Indonesian', "value": 'DeuteroMalayid'}, 
{ "label": 'Neo Melanesid', "value": 'NeoMelanesid'}, 
{ "label": 'Nesid', "value": 'Nesiotid'}, 
{ "label": 'Nesiotid', "value": 'Nesiotid'}, 
{ "label": 'New Caledonian', "value": 'PaleoMelanesid'}, 
{ "label": 'Nilid', "value": 'basic/Nilotid'}, 
{ "label": 'Nilo Hamitic', "value": 'NiloHamitic'}, 
{ "label": 'Nilocharienne', "value": 'basic/Nilotid'}, 
{ "label": 'Nilotes', "value": 'basic/Nilotid'}, 
{ "label": 'Nilotic Negro', "value": 'basic/Nilotid'}, 
{ "label": 'Nilotica', "value": 'basic/Nilotid'}, 
{ "label": 'Nilotid', "value": 'basic/Nilotid'}, 
{ "label": 'Nilotique', "value": 'basic/Nilotid'}, 
{ "label": 'Nord-Atlantique', "value": 'basic/Silvid'}, 
{ "label": 'Nordic', "value": 'basic/Nordid'}, 
{ "label": 'Nordica', "value": 'basic/Nordid'}, 
{ "label": 'Nordid', "value": 'basic/Nordid'}, 
{ "label": 'Nordindid', "value": 'NorthIndid'}, 
{ "label": 'Nordique', "value": 'basic/Nordid'}, 
{ "label": 'Nord-Pacifique', "value": 'basic/Pacifid'}, 
{ "label": 'Norid', "value": 'Norid'}, 
{ "label": 'North Amazonid', "value": 'NorthAmazonid'}, 
{ "label": 'North Andamanid', "value": 'NorthAndamanid'}, 
{ "label": 'North Andid', "value": 'NorthAndid'}, 
{ "label": 'North Atlantid', "value": 'NorthAtlantid'}, 
{ "label": 'North Australid', "value": 'NorthAustralid'}, 
{ "label": 'North Bantuid', "value": 'NorthBantuid'}, 
{ "label": 'North Chinese   ', "value": 'Huanghoid'}, 
{ "label": 'North Eritrean', "value": 'Danakil'}, 
{ "label": 'North Ethiopid', "value": 'NorthEthiopid'}, 
{ "label": 'North Gondid', "value": 'NorthGondid'}, 
{ "label": 'North Indid', "value": 'NorthIndid'}, 
{ "label": 'North Lappid', "value": 'NorthLappid'}, 
{ "label": 'North Pampid', "value": 'Bororo'}, 
{ "label": 'North Pontid', "value": 'NorthPontid'}, 
{ "label": 'North Sinid', "value": 'Huanghoid'}, 
{ "label": 'North Western', "value": 'NorthAtlantid'}, 
{ "label": 'NorthBrasilid', "value": 'NorthAmazonid'}, 
{ "label": 'Northeast European', "value": 'basic/EastEuropid'}, 
{ "label": 'Norwegian Alpinoid', "value": 'Strandid'}, 
{ "label": 'Obid', "value": 'Uralid'}, 
{ "label": 'Oby', "value": 'Uralid'}, 
{ "label": 'Oceanique', "value": 'basic/Polynesid'}, 
{ "label": 'Okayama', "value": 'ManchuKorean'}, 
{ "label": 'Omotic', "value": 'Omotic'}, 
{ "label": 'Onega-Saimen', "value": 'Savolaxid'}, 
{ "label": 'Onghi', "value": 'SouthAndamanid'}, 
{ "label": 'Oriental', "value": 'NeoDanubian'}, 
{ "label": 'Orientalid', "value": 'basic/Orientalid'}, 
{ "label": 'Oromonica ', "value": 'CentralEthiopid'}, 
{ "label": 'Östbaltisk', "value": 'basic/EastEuropid'}, 
{ "label": 'Ostbrasilid', "value": 'basic/Lagid'}, 
{ "label": 'Østerdal', "value": 'Hallstatt'}, 
{ "label": 'Osteuropid', "value": 'basic/EastEuropid'}, 
{ "label": 'Ottentotta', "value": 'Khoid'}, 
{ "label": 'Pacific', "value": 'basic/Pacifid'}, 
{ "label": 'Pacifid', "value": 'Pacifid'}, 
{ "label": 'Pacifid', "value": 'basic/Pacifid'}, 
{ "label": 'Padana', "value": 'Litorid'}, 
{ "label": 'Palaenegrid 2', "value": 'Guinesid'}, 
{ "label": 'Palaenegrid 3', "value": 'EquatorialSudanid'}, 
{ "label": 'Palänegrid', "value": 'basic/Congolid'}, 
{ "label": 'Palänegrid 1', "value": 'Congolesid'}, 
{ "label": 'Palänegrid 4', "value": 'MountainDama'}, 
{ "label": 'Palaungid', "value": 'Palaungid'}, 
{ "label": 'Paleo Atlantid', "value": 'PaleoAtlantid'}, 
{ "label": 'Paleo Melanesid', "value": 'PaleoMelanesid'}, 
{ "label": 'Paleo Negrid', "value": 'basic/Congolid'}, 
{ "label": 'Paleo Saharid', "value": 'PaleoSaharid'}, 
{ "label": 'Paleo Sardinian', "value": 'PaleoSardinian'}, 
{ "label": 'Paleo Siberian', "value": 'Yenisey'}, 
{ "label": 'Paléo-Amérind', "value": 'basic/Lagid'}, 
{ "label": 'Paléo-Amérindienne', "value": 'basic/Lagid'}, 
{ "label": 'Paleoindid', "value": 'basic/IndoMelanid'}, 
{ "label": 'Paleosiberiana', "value": 'basic/Sibirid'}, 
{ "label": 'Paléosibérienne', "value": 'basic/Sibirid'}, 
{ "label": 'Pamir', "value": 'EastPamirid'}, 
{ "label": 'Pamirid', "value": 'CentralPamirid'}, 
{ "label": 'Pamiro-Ferghan', "value": 'basic/Turanid'}, 
{ "label": 'Pampid', "value": 'Pampid'}, 
{ "label": 'Pannonid', "value": 'Gorid'}, 
{ "label": 'Papouasienne', "value": 'basic/Melanesid'}, 
{ "label": 'Papuan', "value": 'NeoMelanesid'}, 
{ "label": 'Papuasid', "value": 'NeoMelanesid'}, 
{ "label": 'Papuid', "value": 'NeoMelanesid'}, 
{ "label": 'Patagonian', "value": 'Patagonid'}, 
{ "label": 'Patagonian', "value": 'basic/Patagonid'}, 
{ "label": 'Patagonid', "value": 'Patagonid'}, 
{ "label": 'Pazifid', "value": 'basic/Pacifid'}, 
{ "label": 'Peninsular Indian', "value": 'GracileIndid'}, 
{ "label": 'Pigmidi', "value": 'basic/Bambutid'}, 
{ "label": 'Plains Pamirid', "value": 'PlainsPamirid'}, 
{ "label": 'Planid', "value": 'Planid'}, 
{ "label": 'Polesian', "value": 'NorthPontid'}, 
{ "label": 'Polinesiana', "value": 'basic/Polynesid'}, 
{ "label": 'Polynesian', "value": 'basic/Polynesid'}, 
{ "label": 'Polynesid', "value": 'basic/Polynesid'}, 
{ "label": 'Polynésienne', "value": 'basic/Polynesid'}, 
{ "label": 'Pontic Mediterreanean', "value": 'Pontid'}, 
{ "label": 'Pontic-Zabrossian', "value": 'Armenid'}, 
{ "label": 'Pontid', "value": 'Pontid'}, 
{ "label": 'Pre Nilotid', "value": 'PreNilotid'}, 
{ "label": 'Pre Slavic', "value": 'PreSlavic'}, 
{ "label": 'Proto Alpine', "value": 'EastAlpinid'}, 
{ "label": 'Proto Ethiopid', "value": 'ProtoEthiopid'}, 
{ "label": 'Proto Eurafricanid', "value": 'Berberid'}, 
{ "label": 'Proto Iranid', "value": 'ProtoIranid'}, 
{ "label": 'Proto Malayid', "value": 'ProtoMalayid'}, 
{ "label": 'Proto Nordid', "value": 'ProtoNordid'}, 
{ "label": 'Pueblid ', "value": 'Pueblid'}, 
{ "label": 'Pueblo-Andida', "value": 'basic/Andid'}, 
{ "label": 'Pueblo-Ándidos', "value": 'basic/Andid'}, 
{ "label": 'Pugliese', "value": 'GracileMediterranid'}, 
{ "label": 'Punan', "value": 'Dayakid'}, 
{ "label": 'Pygméenne', "value": 'basic/Bambutid'}, 
{ "label": 'Rhodesoid', "value": 'Katangid'}, 
{ "label": 'Riffian', "value": 'Canarid'}, 
{ "label": 'Robust Polynesid', "value": 'RobustPolynesid'}, 
{ "label": 'Ryazan', "value": 'NorthPontid'}, 
{ "label": 'Saharan Ethiopid', "value": 'SaharanEthiopid'}, 
{ "label": 'Sahariana', "value": 'SaharanEthiopid'}, 
{ "label": 'Saharid', "value": 'TransMediterranid'}, 
{ "label": 'Samoyedic', "value": 'Samoyedic'}, 
{ "label": 'Sandawe', "value": 'Sandawe'}, 
{ "label": 'Sanid', "value": 'basic/Sanid'}, 
{ "label": 'Sarmatian', "value": 'AndronovoTuranid'}, 
{ "label": 'Satsuma', "value": 'Satsuma'}, 
{ "label": 'Savid', "value": 'Dinarid'}, 
{ "label": 'Savolaxid', "value": 'Savolaxid'}, 
{ "label": 'Scando Lappid', "value": 'ScandoLappid'}, 
{ "label": 'Sciari', "value": 'Shari'}, 
{ "label": 'Scytho-Dravidian', "value": 'IndoBrachid '}, 
{ "label": 'Selvasid', "value": 'Huarpid'}, 
{ "label": 'Semangid', "value": 'Semangid'}, 
{ "label": 'Semangid', "value": 'Semangid'}, 
{ "label": 'Semi-Marginal', "value": 'basic/Lagid'}, 
{ "label": 'Semite', "value": 'basic/Orientalid'}, 
{ "label": 'Semitic', "value": 'Arabid'}, 
{ "label": 'Senegalid', "value": 'Senegalid'}, 
{ "label": 'Senoid', "value": 'Senoid'}, 
{ "label": 'Shanid', "value": 'Shanid'}, 
{ "label": 'Shari', "value": 'Shari'}, 
{ "label": 'Sharid', "value": 'Shari'}, 
{ "label": 'Shillukid', "value": 'Shillukid'}, 
{ "label": 'Sibérienne', "value": 'basic/Sibirid'}, 
{ "label": 'Sibirid', "value": 'basic/Sibirid'}, 
{ "label": 'Silvestre', "value": 'basic/Congolid'}, 
{ "label": 'Silvid', "value": 'basic/Silvid'}, 
{ "label": 'Silvoid Centralid', "value": 'Pueblid '}, 
{ "label": 'Sinhalesid', "value": 'Sinhalesid'}, 
{ "label": 'Sinica centrale', "value": 'Changkiangid'}, 
{ "label": 'Sino-Europid', "value": 'Tibetid'}, 
{ "label": 'Siwa', "value": 'Siwa'}, 
{ "label": 'Skando Lappid', "value": 'ScandoLappid'}, 
{ "label": 'Skando Nordid', "value": 'Hallstatt'}, 
{ "label": 'Small Mediterranean', "value": 'GracileMediterranid'}, 
{ "label": 'Sonoran', "value": 'Sonorid'}, 
{ "label": 'Sonorid', "value": 'Sonorid'}, 
{ "label": 'Soudano-Guinéen', "value": 'SudanoGuinesid'}, 
{ "label": 'South African', "value": 'basic/Bantuid'}, 
{ "label": 'South Africanid', "value": 'basic/Bantuid'}, 
{ "label": 'South Amazonid', "value": 'SouthAmazonid'}, 
{ "label": 'South Andamanid', "value": 'SouthAndamanid'}, 
{ "label": 'South Andid', "value": 'SouthAndid'}, 
{ "label": 'South Arabian', "value": 'ArabianVeddoid'}, 
{ "label": 'South Arabid', "value": 'Yemenid'}, 
{ "label": 'South Atlantid', "value": 'basic/Patagonid'}, 
{ "label": 'South Australid', "value": 'SouthAustralid'}, 
{ "label": 'South Bantuid', "value": 'SouthBantuid'}, 
{ "label": 'South Brasilid', "value": 'SouthAmazonid'}, 
{ "label": 'South Ethiopid', "value": 'SouthEthiopid'}, 
{ "label": 'South Fuegid', "value": 'SouthFuegid'}, 
{ "label": 'South Gondid', "value": 'SouthGondid'}, 
{ "label": 'South Kaffrid', "value": 'SouthBantuid'}, 
{ "label": 'South Lappid', "value": 'ScandoLappid'}, 
{ "label": 'South Nilotid', "value": 'SouthNilotid'}, 
{ "label": 'South Oriental', "value": 'Arabid'}, 
{ "label": 'South Pacifid', "value": 'Arizonid'}, 
{ "label": 'South Palaungid', "value": 'SouthPalaungid'}, 
{ "label": 'South Polynesid', "value": 'SouthPolynesid'}, 
{ "label": 'South Siberian', "value": 'Aralid'}, 
{ "label": 'South Siberian (Kazakhstanian)', "value": 'Aralid'}, 
{ "label": 'South Siberian (northwestern)', "value": 'Aralid'}, 
{ "label": 'Southeastern South Siberian', "value": 'MountainAralid'}, 
{ "label": 'Southern Indian', "value": 'basic/IndoMelanid'}, 
{ "label": 'Strandid', "value": 'Strandid'}, 
{ "label": 'Strandlooper', "value": 'Strandlooper'}, 
{ "label": 'Sub Adriatic', "value": 'Norid '}, 
{ "label": 'Sub Lappid', "value": 'NorthLappid'}, 
{ "label": 'Sub Uralic', "value": 'Volgid'}, 
{ "label": 'Subandids', "value": 'Huarpid'}, 
{ "label": 'Subarktid', "value": 'Athabaskid'}, 
{ "label": 'Subnordid', "value": 'Tavastid'}, 
{ "label": 'Sudanid', "value": 'Sudanid'}, 
{ "label": 'Sudano Guinesid', "value": 'SudanoGuinesid'}, 
{ "label": 'Sudetic', "value": 'PreSlavic'}, 
{ "label": 'Sud-Orientale', "value": 'basic/Orientalid'}, 
{ "label": 'Sud-Pacifique', "value": 'basic/Andid'}, 
{ "label": 'Sud-Pacifique', "value": 'basic/Centralid'}, 
{ "label": 'Syrid', "value": 'Assyroid'}, 
{ "label": 'Taigid', "value": 'Baykal'}, 
{ "label": 'Tamil', "value": 'Karnatid'}, 
{ "label": 'Tamild', "value": 'Karnatid'}, 
{ "label": 'Tapirid', "value": 'Tapirid'}, 
{ "label": 'Tapiro', "value": 'Tapirid'}, 
{ "label": 'Targid', "value": 'Targid'}, 
{ "label": 'Tasmanid', "value": 'Tasmanid'}, 
{ "label": 'Tasmanoid', "value": 'Barrinean'}, 
{ "label": 'Taurid', "value": 'basic/Dinarid'}, 
{ "label": 'Tavast', "value": 'Tavastid'}, 
{ "label": 'Tavastid', "value": 'Tavastid'}, 
{ "label": 'Teuto Nordid ', "value": 'Hallstatt'}, 
{ "label": 'Thracian', "value": 'Pontid'}, 
{ "label": 'Tibetan', "value": 'Tibetid'}, 
{ "label": 'Tibetan-Sino-Indochinese', "value": 'Shanid'}, 
{ "label": 'Tibetid', "value": 'Tibetid'}, 
{ "label": 'Tien Shanian', "value": 'MountainAralid'}, 
{ "label": 'Toalid', "value": 'Toalid'}, 
{ "label": 'Toda', "value": 'Toda '}, 
{ "label": 'Tonkinesid', "value": 'Tonkinesid'}, 
{ "label": 'Trans Mediterranid', "value": 'TransMediterranid'}, 
{ "label": 'Transcaspian', "value": 'Transcaspian'}, 
{ "label": 'Trønder ', "value": 'Tronder'}, 
{ "label": 'Tropical', "value": 'basic/Congolid'}, 
{ "label": 'Tsong-Tonga  ', "value": 'CentralBantuid'}, 
{ "label": 'Turko Iranian', "value": 'IndoIranid'}, 
{ "label": 'Turkoman', "value": 'Transcaspian'}, 
{ "label": 'Turko-Tatar ', "value": 'Aralid'}, 
{ "label": 'Tutsi', "value": 'SouthEthiopid'}, 
{ "label": 'Twa-Cwa', "value": 'TwaCwa'}, 
{ "label": 'Twid', "value": 'EastBambutid'}, 
{ "label": 'Tydal', "value": 'PaleoAtlantid'}, 
{ "label": 'Upper Nile', "value": 'Shillukid '}, 
{ "label": 'Upper Paleolithic', "value": 'PaleoAtlantid'}, 
{ "label": 'Uralic', "value": 'Uralid'}, 
{ "label": 'Uralid', "value": 'Uralid'}, 
{ "label": 'Valdai', "value": 'Tavastid'}, 
{ "label": 'Varid', "value": 'ScandoLappid'}, 
{ "label": 'Västmanland', "value": 'Dalofaelid'}, 
{ "label": 'Vedda', "value": 'Vedda'}, 
{ "label": 'Vistulan', "value": 'PreSlavic'}, 
{ "label": 'Volga Kama', "value": 'Volgid'}, 
{ "label": 'Volgid', "value": 'Volgid'}, 
{ "label": 'West Alpinid', "value": 'WestAlpinid'}, 
{ "label": 'West Amazonid', "value": 'WestAmazonid'}, 
{ "label": 'West Baltic', "value": 'Borreby'}, 
{ "label": 'West Bambutid', "value": 'WestBambutid'}, 
{ "label": 'West Brachid', "value": 'IndoBrachid '}, 
{ "label": 'West Brasilid', "value": 'WestAmazonid'}, 
{ "label": 'West Congolesid', "value": 'WestCongolesid'}, 
{ "label": 'West Ethiopid', "value": 'WestEthiopid'}, 
{ "label": 'West forest', "value": 'WestCongolesid'}, 
{ "label": 'West Mediterranid', "value": 'GracileMediterranid'}, 
{ "label": 'West Negrillo', "value": 'WestBambutid'}, 
{ "label": 'West Nilotid', "value": 'Shari'}, 
{ "label": 'West Pyrenean', "value": 'Baskid'}, 
{ "label": 'West Sibirid', "value": 'basic/Sibirid'}, 
{ "label": 'West Sibirird', "value": 'Uralid'}, 
{ "label": 'West Twid', "value": 'WestBambutid'}, 
{ "label": 'Western [Africa]', "value": 'Casamance'}, 
{ "label": 'Western [Europe]', "value": 'GracileMediterranid'}, 
{ "label": 'Western Desert', "value": 'DesertAustralid'}, 
{ "label": 'Western European', "value": 'basic/Alpinid'}, 
{ "label": 'Wüstenländisch', "value": 'basic/Orientalid'}, 
{ "label": 'Xhosaid', "value": 'Xhosaid'}, 
{ "label": 'Xhosa-Sotho-Shangana', "value": 'Xhosaid'}, 
{ "label": 'Yakonin', "value": 'Yakonin'}, 
{ "label": 'Yemenic Mediterranean', "value": 'Yemenid'}, 
{ "label": 'Yemenid', "value": 'Yemenid'}, 
{ "label": 'Yenisey', "value": 'Yenisey'}, 
{ "label": 'Yuki ', "value": 'Californid'}, 
{ "label": 'Zambesid', "value": 'basic/Bantuid'}, 
{ "label": 'Zentralid', "value": 'basic/Centralid'}, 
{ "label": 'Sinid', "value": 'basic/Sinid'}, 
{ "label": 'Far Eastern', "value": 'basic/Sinid'}, 
{ "label": 'Centro-Mongole', "value": 'basic/Sinid'}, 
{ "label": 'Sinienne', "value": 'basic/Sinid'}, 
{ "label": 'Homo sinicus', "value": 'basic/Sinid'}, 
{ "label": 'Pareid', "value": 'basic/South Mongolid'}, 
{ "label": 'South Mongolid', "value": 'basic/South Mongolid'}, 
{ "label": 'Nesid', "value": 'basic/South Mongolid'}, 
{ "label": 'Palämongolid', "value": 'basic/South Mongolid'}, 
{ "label": 'Paleo Mongolid', "value": 'basic/South Mongolid'}, 
{ "label": 'Sud-Mongole', "value": 'basic/South Mongolid'}, 
{ "label": 'Sudmongolica', "value": 'basic/South Mongolid'}, 
{ "label": 'Indonesian-Malay', "value": 'basic/South Mongolid'}, 
{ "label": 'Southeast Asiatic', "value": 'basic/South Mongolid'}, 
{ "label": 'Southern Mongoloid', "value": 'basic/South Mongolid'}, 
{ "label": 'Sudanid', "value": 'basic/Sudanid'}, 
{ "label": 'Sudanese', "value": 'basic/Sudanid'}, 
{ "label": 'Soudanaise', "value": 'basic/Sudanid'}, 
{ "label": 'Sudanian', "value": 'basic/Sudanid'}, 
{ "label": 'West African Negro', "value": 'basic/Sudanid'}, 
{ "label": 'Homo sudanensis', "value": 'basic/Sudanid'}, 
{ "label": 'Tungid', "value": 'basic/Tungid'}, 
{ "label": 'Nord-Mongole', "value": 'basic/Tungid'}, 
{ "label": 'Northern Asiatic', "value": 'basic/Tungid'}, 
{ "label": 'Altaid', "value": 'basic/Tungid'}, 
{ "label": 'Classic Mongoloid', "value": 'basic/Tungid'}, 
{ "label": 'Tungusa', "value": 'basic/Tungid'}, 
{ "label": 'Toungouzienne', "value": 'basic/Tungid'}, 
{ "label": 'Homo tataturs', "value": 'basic/Tungid'}, 
{ "label": 'Turanid', "value": 'basic/Turanid'}, 
{ "label": 'Touranienne', "value": 'basic/Turanid'}, 
{ "label": 'Turkic', "value": 'basic/Turanid'}, 
{ "label": 'Central-Asiatic-Inter-River', "value": 'basic/Turanid'}, 
{ "label": 'Homo eurasicus', "value": 'basic/Turanid'}, 
{ "label": 'Veddid', "value": 'basic/Veddid'}, 
{ "label": 'Weddid', "value": 'basic/Veddid'}, 
{ "label": 'Veddoid', "value": 'basic/Veddid'}, 
{ "label": 'Ceylonesian-Sundanesian', "value": 'basic/Veddid'}, 
{ "label": 'Homo veddalis', "value": 'basic/Veddid'}, 
{ "label": 'East Mediterranid', "value": 'Pontid'}, 
{ "label": 'Paranegrid', "value": 'basic/Ethiopid'}, 
{ "label": 'Pareid', "value": 'basic/SouthMongolid'}, 
{ "label": 'Nesid', "value": 'basic/SouthMongolid'}, 
{ "label": 'Fumid', "value": 'SouthEthiopid'}, 
{ "label": 'Koptid', "value": 'Egyptid'}
]

class FaceRecognitionDatabase:
    def __init__(self, faces_dir="./faces", database_file="face_database.pkl"):
        """
        Initialize the face recognition database.
        
        Args:
            faces_dir (str): Directory containing face images
            database_file (str): File to save/load the face encodings database
        """
        self.faces_dir = Path(faces_dir)
        self.database_file = database_file
        self.known_face_encodings = []
        self.known_face_names = []
        
    def build_database(self, force_rebuild=False):
        """
        Build a database of face encodings from images in the faces directory.
        
        Args:
            force_rebuild (bool): If True, rebuild the database even if it exists
            
        Returns:
            bool: True if database was built or loaded successfully
        """
        # Check if database file already exists
        if os.path.exists(self.database_file) and not force_rebuild:
            print(f"Loading existing face database from {self.database_file}")
            try:
                with open(self.database_file, 'rb') as f:
                    data = pickle.load(f)
                    self.known_face_encodings = data['encodings']
                    self.known_face_names = data['names']
                print(f"Loaded {len(self.known_face_names)} face encodings")
                return True
            except Exception as e:
                print(f"Error loading database: {e}")
                print("Building new database...")
        
        # Create faces directory if it doesn't exist
        self.faces_dir.mkdir(exist_ok=True)
        
        # Get list of image files
        image_files = []
        for ext in ["*.jpg", "*.jpeg", "*.png"]:
            image_files.extend(list(self.faces_dir.glob(ext)))
        
        if not image_files:
            print(f"No image files found in {self.faces_dir}")
            return False
        
        # Process each image
        for img_path in image_files:
            name = img_path.stem  # Get filename without extension
            try:
                # Load image
                image = face_recognition.load_image_file(img_path)
                
                # Find face locations and encodings
                face_locations = face_recognition.face_locations(image)
                
                if not face_locations:
                    print(f"No face found in {img_path}. Skipping.")
                    continue
                
                # Use the first face found in the image
                face_encoding = face_recognition.face_encodings(image, face_locations)[0]
                
                # Add to database
                self.known_face_encodings.append(face_encoding)
                self.known_face_names.append(name)
                print(f"Added face: {name}")
                
            except Exception as e:
                print(f"Error processing {img_path}: {e}")
        
        # Save database to file
        if self.known_face_encodings:
            try:
                with open(self.database_file, 'wb') as f:
                    pickle.dump({
                        'encodings': self.known_face_encodings,
                        'names': self.known_face_names
                    }, f)
                print(f"Saved {len(self.known_face_names)} face encodings to {self.database_file}")
                return True
            except Exception as e:
                print(f"Error saving database: {e}")
                return False
        else:
            print("No faces were encoded. Database not created.")
            return False
    
    def compare_face(self, image_path, top_n=10):
        """
        Compare a face image with all faces in the database and return the top N most similar faces.
        Always returns similarity scores regardless of how similar or different the faces are.
        
        Args:
            image_path (str): Path to the image to compare
            top_n (int): Number of top similar faces to return
            
        Returns:
            list: List of tuples (name, similarity_percentage) sorted by similarity (highest first)
        """
        if not self.known_face_encodings:
            print("Database is empty. Build database first.")
            return []
        
        try:
            # Load the image
            image = face_recognition.load_image_file(image_path)
            
            # Find face locations and encodings
            face_locations = face_recognition.face_locations(image)
            
            if not face_locations:
                print(f"Warning: No face detected in {image_path}. Using the entire image instead.")
                # If no face is detected, use the whole image and try to encode it anyway
                # This might not give accurate results but will allow comparison
                face_encoding = face_recognition.face_encodings(image)[0] if face_recognition.face_encodings(image) else None
                
                if face_encoding is None:
                    print(f"Error: Could not generate encoding from {image_path}")
                    return []
            else:
                # Use the first face found
                face_encoding = face_recognition.face_encodings(image, face_locations)[0]
            
            # Calculate face distances
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            
            # Convert distances to similarity scores (0-100%)
            # The lower the distance, the higher the similarity
            similarity_scores = [(1 - dist) * 100 for dist in face_distances]
            
            # Create list of (name, similarity) tuples
            results = list(zip(self.known_face_names, similarity_scores))
            
            # Sort by similarity (highest first)
            results.sort(key=lambda x: x[1], reverse=True)
            
            # Always return results, even if similarity is low
            # This ensures we see how far X.jpg is from each face in the database
            return results[:top_n]
            
        except Exception as e:
            print(f"Error comparing face: {e}")
            return []

def resolve(name):
    labels = {}
    for l in data:
        d = l["value"].replace("basic/", "").lower()
        labels[d] = l["label"]
    name_edit = name[:-1]
    if name_edit in labels:
        return labels[name_edit]
    return name_edit

def compare(test_image):
    # Initialize and build the database
    db = FaceRecognitionDatabase()
    db.build_database()

    # Example: Compare a new face against the database
    results = db.compare_face(test_image)

    print(f"\nTop 10 most similar faces to {test_image}:")
    if results:
        for name, similarity in results:
            print(f"{resolve(name)}:")
            print(f"{similarity:.2f}% similarity\n")
    else:
        print(f"Could not process {test_image} for comparison")

def download():
    import os

    pre = 'https://humanphenotypes.net/'
    ref = 'wget @ --no-check-certificate --user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"'

    links = []
    for d in data:
        val = pre + d["value"].replace(' ', '').strip().lower() + "f.jpg"
        if val not in links:
            links.append(val)

    for l in links:
        try:
            os.system(ref.replace("@", l))
        except Exception as e:
            print(str(e))