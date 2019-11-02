import os
import unittest
from read import Read
from read.range import Range
from .WikipediaItem import WikipediaItem

DBWIKIPEDIA = "tests/data/wikipedia.db"


class MyTestCase(unittest.TestCase):
    def setUp(self):
        ...


    def test_1_connection(self):
        r = Read( DBWIKIPEDIA )
        #self.assertIsInstance( r, Range )


    def test_2_db_rows(self):
        for row in Read( DBWIKIPEDIA ):
            self.assertTupleEqual( row, ('en§Cat§DISAMBIGUATION_INDEF_INDEF_DOMESTICATED§0', 'Cat', 'DISAMBIGUATION_INDEF_INDEF_DOMESTICATED', 'en', 'The cat (Felis catus) is a small carnivorous mammal. It is the only domesticated species in the family Felidae and often referred to as the domestic cat to distinguish it from wild members of the family. The cat is either a house cat or a farm cat, which are pets, or a feral cat, which ranges freely and avoids human contact.\nA house cat is valued by humans for companionship and for its ability to hunt rodents. About 60 cat breeds are recognized by various cat registries.\n\nThe cat is similar in anatomy to the other felid species, has a strong flexible body, quick reflexes, sharp teeth and retractable claws adapted to killing small prey. Its night vision and sense of smell are well developed. Cat communication includes vocalizations like meowing, purring, trilling, hissing, growling and grunting as well as cat-specific body language. It is a solitary hunter, but a social species. It can hear sounds too faint or too high in frequency for human ears, such as those made by mice and other small mammals. It is a predator that is most active at dawn and dusk. It secretes and perceives pheromones.\n\nFemale domestic cats can have kittens from spring to late autumn, with litter sizes ranging from two to five kittens. \nDomestic cats are bred and shown as registered pedigreed cats, a hobby known as cat fancy. Failure to control breeding of pet cats by spaying and neutering, as well as abandonment of pets, resulted in large numbers of feral cats worldwide, contributing to the extinction of entire bird species, and evoking population control.\n\nIt was long thought that cat domestication was initiated in Egypt, because cats in ancient Egypt were venerated since around 3100 BC.\nHowever, the earliest indication for the taming of an African wildcat (F. lybica) was found in Cyprus, where a cat skeleton was excavated close by a human Neolithic grave dating to around 7500 BC. African wildcats were probably first domesticated in the Near East.\n\nAs of 2017, the domestic cat was the second-most popular pet in the U.S. by number of pets owned, after freshwater fish, with 95 million cats owned. In the United Kingdom, around 7.3 million cats lived in more than 4.8 million households as of 2019.', '\n{{about|the cat species that is commonly kept as a pet|the cat family|Felidae|other uses|Cat (disambiguation)|and|Cats (disambiguation)}}\n{{pp-semi-indef|small=yes}}\n{{pp-move-indef|small=yes}}\n{{short description|Domesticated feline}}\n{{technical reasons|Cat #1|the album|Cat 1 (album)}}\n{{Use dmy dates|date=February 2019}}\n{{Good article}}\n\n{{Speciesbox\n|name= Domestic cat\n|status= DOM\n<!-- There has been extensive discussion about the choice of image in this infobox. Before replacing this image with something else, consider if it actually improves on the ENCYCLOPEDIC CRITERIA which led to this choice. See [[Talk:Cat]] and [[Talk:Cat/Lead photo]] and if in doubt, DISCUSS IT FIRST! -->\n|image = Cat poster 1.jpg<!--please do not change without consensus, see talk page-->\n|image_upright = 1.2\n|image_caption = Various types of domestic cat\n|genus = Felis\n|species = catus<ref name="Linaeus1758">{{Cite book |last=Linnaeus |first=C. |title=Systema naturae per regna tria naturae: secundum classes, ordines, genera, species, cum characteribus, differentiis, synonymis, locis |location=Holmiae |publisher=Laurentii Salvii |year=1758 |page=42 |chapter=Felis Catus |language=Latin |volume=1 |edition=Tenth reformed |chapterurl=https://archive.org/details/mobot31753000798865/page/42}}</ref>\n|authority =([[Carl Linnaeus|Linnaeus]], [[10th edition of Systema Naturae|1758]])<ref name="MSW3fc" />\n|synonyms=\n*\'\'F. catus domesticus\'\' {{small|Erxleben, 1777}}<ref name=Erxleben>{{Cite book |last=Erxleben |first=J. C. P. |year=1777 |title=Systema regni animalis per classes, ordines, genera, species, varietates cvm synonymia et historia animalivm. Classis I. Mammalia |location=Lipsiae |publisher=Weygandt |pages=520–521 |chapter=Felis Catus domesticus |chapterurl=https://archive.org/details/iochristpolycerx00erxl/page/520}}</ref>\n*\'\'F. angorensis\'\' {{small|[[Karl Christian Gmelin|Gmelin]], 1788}}\n*\'\'F. vulgaris\'\' {{small|Fischer, 1829}}\n}}\nThe \'\'\'cat\'\'\' (\'\'Felis catus\'\') is a small [[carnivorous]] [[mammal]]. It is the only [[domesticated]] [[Species (biological)|species]] in the family [[Felidae]] and often referred to as the \'\'\'domestic cat\'\'\' to distinguish it from wild members of the [[Family (biology)|family]]. The cat is either a \'\'\'house cat\'\'\' or a \'\'\'[[farm cat]]\'\'\', which are [[pet]]s, or a \'\'\'[[feral cat]]\'\'\', which ranges freely and avoids human contact.\nA house cat is valued by [[human]]s for companionship and for its ability to hunt [[rodents]]. About 60 [[List of cat breeds|cat breeds]] are recognized by various [[cat registry|cat registries]].\n\nThe cat is similar in [[Cat anatomy|anatomy]] to the other felid species, has a strong flexible body, quick reflexes, sharp teeth and retractable claws adapted to killing small prey. Its [[night vision]] and [[sense of smell]] are well developed. [[Cat communication]] includes [[Animal communication|vocalizations]] like [[meow]]ing, [[purr]]ing, [[Trill consonant|trilling]], hissing, [[growling]] and [[Guttural|grunting]] as well as [[cat-specific body language]]. It is a solitary hunter, but a [[social species]]. It can hear sounds too faint or too high in [[frequency]] for human ears, such as those made by mice and other small mammals. It is a [[predator]] that is most active at dawn and dusk. It secretes and perceives [[pheromones]].\n\nFemale domestic cats can have kittens from spring to late autumn, with litter sizes ranging from two to five kittens. \nDomestic cats are bred and shown as registered [[pedigreed cat]]s, a hobby known as [[cat fancy]]. Failure to control breeding of pet cats by [[spaying]] and [[neutering]], as well as abandonment of pets, resulted in large numbers of feral cats worldwide, contributing to the extinction of entire bird species, and evoking [[Animal population control|population control]].\n\nIt was long thought that cat domestication was initiated in Egypt, because [[cats in ancient Egypt]] were venerated since around 3100 [[Before Christ|BC]].\nHowever, the earliest indication for the [[taming]] of an [[African wildcat]] (\'\'F. lybica\'\') was found in [[Cyprus]], where a cat skeleton was [[Excavation (archaeology)|excavated]] close by a human [[Neolithic]] grave dating to around 7500 BC. African wildcats were probably first domesticated in the [[Near East]].\n \nAs of 2017, the domestic cat was the second-most popular pet in the U.S. by number of pets owned, after [[Fishkeeping#Freshwater|freshwater fish]], with 95 million cats owned. In the United Kingdom, around 7.3 million cats lived in more than 4.8 million households as of 2019.\n', '["Linnaeus", "1758", "Gmelin", "carnivorous", "mammal", "domesticated", "species", "Felidae", "family", "farm cat", "pet", "feral cat", "human", "rodents", "cat breeds", "cat registries", "anatomy", "night vision", "sense of smell", "Cat communication", "vocalizations", "meow", "purr", "trilling", "growling", "grunting", "cat-specific body language", "social species", "frequency", "predator", "pheromones", "pedigreed cat", "cat fancy", "spaying", "neutering", "population control", "Springer Science+Business Media", "cats in ancient Egypt", "BC", "taming", "African wildcat", "Cyprus", "excavated", "Neolithic", "Science", "Near East", "freshwater fish"]', None, None, 'https://en.wikipedia.org/wiki/Cat', '["/wiki/Felidae", "/wiki/Cat_(disambiguation)", "/wiki/Cats_(disambiguation)", "/wiki/Wikipedia:Naming_conventions_(technical_restrictions)#Forbidden_characters", "/wiki/Cat_1_(album)", "/wiki/File:Cat_poster_1.jpg", "/wiki/Conservation_status", "/wiki/Taxonomy_(biology)", "/wiki/Template:Taxonomy/Felis", "/wiki/Animal", "/wiki/Chordate", "/wiki/Mammal", "/wiki/Carnivora", "/wiki/Feliformia", "/wiki/Felidae", "/wiki/Felinae", "/wiki/Felis", "/wiki/Binomial_nomenclature", "/wiki/Carl_Linnaeus", "/wiki/10th_edition_of_Systema_Naturae", "/wiki/Synonym_(taxonomy)", "/wiki/Karl_Christian_Gmelin", "/wiki/Carnivorous", "/wiki/Mammal", "/wiki/Domesticated", "/wiki/Species_(biological)", "/wiki/Felidae", "/wiki/Family_(biology)", "/wiki/Farm_cat", "/wiki/Pet", "/wiki/Feral_cat", "/wiki/Human", "/wiki/Rodents", "/wiki/List_of_cat_breeds", "/wiki/Cat_registry", "/wiki/Cat_anatomy", "/wiki/Night_vision", "/wiki/Sense_of_smell", "/wiki/Cat_communication", "/wiki/Animal_communication", "/wiki/Meow", "/wiki/Purr", "/wiki/Trill_consonant", "/wiki/Growling", "/wiki/Guttural", "/wiki/Cat-specific_body_language", "/wiki/Social_species", "/wiki/Frequency", "/wiki/Predator", "/wiki/Pheromones", "/wiki/Pedigreed_cat", "/wiki/Cat_fancy", "/wiki/Spaying", "/wiki/Neutering", "/wiki/Animal_population_control", "/wiki/Cats_in_ancient_Egypt", "/wiki/Before_Christ", "/wiki/Taming", "/wiki/African_wildcat", "/wiki/Cyprus", "/wiki/Excavation_(archaeology)", "/wiki/Neolithic", "/wiki/Near_East", "/wiki/Fishkeeping#Freshwater"]', '["Felidae", "Cat_(disambiguation)", "Cats_(disambiguation)", "Wikipedia:Naming_conventions_(technical_restrictions)#Forbidden_characters", "Cat_1_(album)", "File:Cat_poster_1.jpg", "Conservation_status", "Taxonomy_(biology)", "Template:Taxonomy/Felis", "Animal", "Chordate", "Mammal", "Carnivora", "Feliformia", "Felinae", "Felis", "Binomial_nomenclature", "Carl_Linnaeus", "10th_edition_of_Systema_Naturae", "Synonym_(taxonomy)", "Karl_Christian_Gmelin", "Carnivorous", "Domesticated", "Species_(biological)", "Family_(biology)", "Farm_cat", "Pet", "Feral_cat", "Human", "Rodents", "List_of_cat_breeds", "Cat_registry", "Cat_anatomy", "Night_vision", "Sense_of_smell", "Cat_communication", "Animal_communication", "Meow", "Purr", "Trill_consonant", "Growling", "Guttural", "Cat-specific_body_language", "Social_species", "Frequency", "Predator", "Pheromones", "Pedigreed_cat", "Cat_fancy", "Spaying", "Neutering", "Animal_population_control", "Cats_in_ancient_Egypt", "Before_Christ", "Taming", "African_wildcat", "Cyprus", "Excavation_(archaeology)", "Neolithic", "Near_East", "Fishkeeping#Freshwater"]', None, None, '["The cat (Felis catus) is a small carnivorous mammal.", "[1][2] It is the only domesticated species in the family Felidae and often referred to as the domestic cat to distinguish it from wild members of the family.", "[4] The cat is either a house cat or a farm cat, which are pets, or a feral cat, which ranges freely and avoids human contact.", "[5]\\nA house cat is valued by humans for companionship and for its ability to hunt rodents.", "About 60 cat breeds are recognized by various cat registries.", "The cat is similar in anatomy to the other felid species, has a strong flexible body, quick reflexes, sharp teeth and retractable claws adapted to killing small prey.", "Cat communication includes vocalizations like meowing, purring, trilling, hissing, growling and grunting as well as cat-specific body language.", "[9] \\nDomestic cats are bred and shown as registered pedigreed cats, a hobby known as cat fancy.", "It was long thought that cat domestication was initiated in Egypt, because cats in ancient Egypt were venerated since around 3100 BC.", "[11][12]\\nHowever, the earliest indication for the taming of an African wildcat (F. lybica) was found in Cyprus, where a cat skeleton was excavated close by a human Neolithic grave dating to around 7500 BC.", "As of 2017, the domestic cat was the second-most popular pet in the U.S. by number of pets owned, after freshwater fish,[15] with 95 million cats owned.", "The origin of the English word \'cat\', Old English catt, is thought to be the Late Latin word cattus, which was first used at the beginning of the 6th century.", "The etymology of this word is unknown, but it may have simply arisen from a sound used to attract a cat.", "The scientific name Felis catus was proposed by Carl Linnaeus in 1758 for a domestic cat.", "[3]\\nFelis daemon proposed by Konstantin Alekseevich Satunin in 1904 was a black cat specimen from the Transcaucasus, later identified as a domestic cat.", "The same commission ruled that the domestic cat is a distinct taxon Felis catus.", "In 2017, the IUCN Cat Classification Taskforce followed the recommendation of the ICZN in regarding the domestic cat as a distinct species.", "The domestic cat is a member of the Felidae, a family that had a common ancestor about 10–15 million years ago.", "[35]\\nResults of phylogenetic research confirm that the wild Felis species evolved through sympatric or parapatric speciation, whereas the domestic cat evolved through artificial selection.", "[36] The domesticated cat and its closest wild ancestor are both diploid organisms that possess 38 chromosomes[37] and roughly 20,000 genes.", "[38]\\nThe leopard cat (Prionailurus bengalensis) was tamed independently in China around 5500 BC.", "This line of partially domesticated cats leaves no trace in the domestic cat populations of today.", "As there is no evidence of native mammalian fauna on Cyprus, the inhabitants of this Neolithic village most likely brought the cat and other wild mammals to the island from the Middle Eastern mainland.", "[14][6] Wildcats of Egypt contributed to the maternal gene pool of the domestic cat at a later time.", "[40]\\nThe earliest known evidence for the occurrence of the domestic cat in Greece dates to around 1200 BC.", "[43]\\nBy the end of the Roman Empire in the 5th century, the Egyptian domestic cat lineage had arrived in a Baltic Sea port in northern Germany.", "[44] House cats often mate with feral cats,[45] producing hybrids such as the Kellas cat in Scotland.", "Development of cat breeds started in the mid 19th century.", "[48]\\nAn analysis of the domestic cat genome revealed that the ancestral wildcat genome was significantly altered in the process of domestication as specific mutations were selected to develop cat breeds.", "The domestic cat has a smaller skull and shorter bones than the European wildcat.", "[53]:11 The extra lumbar and thoracic vertebrae account for the cat\'s spinal mobility and flexibility.", "[53] :16 Unlike human arms, cat forelimbs are attached to the shoulder by free-floating clavicle bones which allow them to pass their body through any space into which they can fit their head.", "The cat skull is unusual among mammals in having very large eye sockets and a powerful specialized jaw.", "When it overpowers its prey, a cat delivers a lethal neck bite with its two long canine teeth, inserting them between two of the prey\'s vertebrae and severing its spinal cord, causing irreversible paralysis and death.", "The cat is digitigrade.", "[55]:43 This is partly the result of cat eyes having a tapetum lucidum, which reflects any light that passes through the retina back into the eye, thereby increasing the eye\'s sensitivity to dim light.", "The domestic cat has slit pupils, which allow it to focus bright light without chromatic aberration.", "[65] At low light, a cat\'s pupils expand to cover most of the exposed surface of its eyes.", "[66] However, the domestic cat has rather poor color vision and only two types of cone cells, optimized for sensitivity to blue and yellowish green; its ability to distinguish between red and green is limited.", "The domestic cat\'s hearing is most acute in the range of 500\xa0Hz to 32\xa0kHz.", "[82]  Cats also have a distinct temperature preference for their food, preferring food with a temperature around 38\xa0°C (100\xa0°F) which is similar to that of a fresh kill and routinely rejecting food presented cold or refrigerated (which would signal to the cat that the \\"prey\\" item is long dead and therefore possibly toxic or decomposing).", "Most breeds of cat have a noted fondness for sitting in high places, or perching.", "Another possible explanation is that height gives the cat a better observation point, allowing it to survey its territory.", "A cat falling from heights of up to 3 meters can right itself and land on its paws.", "[83]\\nDuring a fall from a high place, a cat reflexively twists its body and rights itself to land on its feet using its acute sense of balance and flexibility.", "This reflex is known as the cat righting reflex.", "[84]\\nAn individual cat always rights itself in the same way during a fall, provided it has sufficient time to do so.", "The term \\"cat nap\\" for a short rest refers to the cat\'s tendency to fall asleep (lightly) for a brief period.", "The social behavior of the domestic cat ranges from widely dispersed individuals to feral cat colonies that gather around a food source, based on groups of co-operating females.", "[94][95] Within such groups, one cat is usually dominant over the others.", "[96] Each cat in a colony holds a distinct territory, with sexually active males having the largest territories, which are about 10 times larger than those of female cats and may overlap with several females\' territories.", "Ethologically, the human keeper of a cat functions as a sort of surrogate for the cat\'s mother.", "Tail-raising also indicates the cat\'s position in the group\'s social hierarchy, with dominant individuals raising their tails less often than subordinate ones.", "The cat has no unique anatomical feature that is clearly responsible for the sound.", "[107] The cat\'s tongue has backwards-facing spines about 500\xa0μm long, which are called papillae.", "[109] Among feral cats, the most common reason for cat fighting is competition between two males to mate with a female.", "Lapping at a rate of four times a second, the cat touches the smooth tip of its tongue to the surface of the water, and quickly retracts it like a corkscrew, drawing water upwards.", "[126]\\nCertain species appear more susceptible than others; for example, 30% of house sparrow mortality is linked to the domestic cat.", "[127] In the recovery of ringed robins (Erithacus rubecula) and dunnocks (Prunella modularis), 31% of deaths were a result of cat predation.", "Perhaps the best known element of cats\' hunting behavior, which is commonly misunderstood and often appals cat owners because it looks like torture, is that cats often appear to \\"play\\" with prey by releasing it after capture.", "This cat and mouse behavior is due to an instinctive imperative to ensure that the prey is weak enough to be killed without endangering the cat.", "[130]\\nAnother poorly understood element of cat hunting behavior is the presentation of prey to human guardians.", "[131] Another explanation is that they attempt to teach their guardians to hunt or to help their human as if feeding \\"an elderly cat, or an inept kitten\\".", "On islands, birds can contribute as much as 60% of a cat\'s diet.", "[133] In nearly all cases, however, the cat cannot be identified as the sole cause for reducing the numbers of island birds, and in some instances, eradication of cats has caused a \\"mesopredator release\\" effect;[134] where the suppression of top carnivores creates an abundance of smaller predators that cause a severe decline in their shared prey.", "[141] String is often used as a toy, but if it is eaten, it can become caught at the base of the cat\'s tongue and then move into the intestines, a medical emergency which can cause serious illness, even death.", "The female utters a loud yowl as the male pulls out of her because a male cat\'s penis has a band of about 120–150 backwards-pointing penile spines, which are about 1\xa0mm (0.039\xa0in) long; upon withdrawal of the penis, the spines rake the walls of the female\'s vagina, which acts to induce ovulation.", "[156] Some cats have been reported as surviving into their 30s,[157] with the oldest known cat, Creme Puff, dying at a verified age of 38.", "[154]:35 Having a cat neutered confers health benefits, because castrated males cannot develop testicular cancer, spayed females cannot develop uterine or ovarian cancer, and both have a reduced risk of mammary cancer.", "The domestic cat is a cosmopolitan species and occurs across much of the world.", "[175] Famous feral cat colonies are found in Rome around the Colosseum and Forum Romanum, with cats at some of these sites being fed and given medical attention by volunteers.", "[177] One common approach to reducing the feral cat population is termed \\"trap-neuter-return\\", where the cats are trapped, neutered, immunized against diseases such as rabies and the feline Panleukopenia and Leukemia viruses, and then released.", "[179] Although cat guardianship has commonly been associated with women, a 2007 Gallup poll reported that men and women in the United States of America were equally likely to own a cat.", "As well as being kept as pets, cats are also used in the international fur[181] and leather industries for making coats, hats, blankets, and stuffed toys;[182] and shoes, gloves, and musical instruments respectively[183] (about 24 cats are needed to make a cat-fur coat).", "[185] Cat pelts have been used for superstitious purposes as part of the practise of witchcraft,[186] and are still made into blankets in Switzerland as folk remedies believed to help rheumatism.", "[187] In the Western intellectual tradition, the idea of cats as everyday objects have served to illustrate problems of quantum mechanics in the Schrödinger\'s cat thought experiment.", "A few attempts to build a cat census have been made over the years, both through associations or national and international organizations (such as the Canadian Federation of Humane Societies\'s one[188]) and over the Internet,[189][190] but such a task does not seem simple to achieve.", "A cat show is a judged event in which the owners of cats compete to win titles in various cat registering organizations by entering their cats to be judged after a breed standard.", "[200] In some cases, the cat exhibits no symptoms of the disease,[201] However, the same disease can then become evident in a human.", "Humans who have cats living in their home or in close association are more likely to become infected, however, those who do not keep cats as pets might also acquire infections from cat feces and parasites exiting the cat\'s body.", "[200][202] Some of the infections of most concern include salmonella, cat-scratch disease and toxoplasmosis.", "In ancient Egypt, cats were worshipped, and the goddess Bastet often depicted in cat form, sometimes taking on the war-like aspect of a lioness.", "The Greek historian Herodotus reported that killing a cat was forbidden, and when a household cat died, the entire family mourned and shaved their eyebrows.", "The usual ancient Greek word for \'cat\' was ailouros, meaning \\"thing with the waving tail\\".", "In Ovid\'s Metamorphoses, when the deities flee to Egypt and take animal forms, the goddess Diana turns into a cat.", "Cats are often shown in icons of Annunciation and of the Holy Family and, according to Italian folklore, on the same night that Mary gave birth to Jesus, a virgin cat in Bethlehem gave birth to a kitten.", "In Japan, the maneki neko cat is a symbol of good fortune.", "[208] In Jewish legend, the first cat was living in the house of the first man Adam as a pet that got rid of mice.", "The cat was once partnering with the first dog before the latter broke an oath they had made which resulted in enmity between the descendants of these two animals.", "Some Western writers have stated Muhammad had a favorite cat, Muezza.", "An example would be the belief that a black cat \\"crossing one\'s path\\" leads to bad luck, or that cats are witches\' familiars used to augment a witch\'s powers and skills.", "The killing of cats in Medieval Ypres, Belgium, is commemorated in the innocuous present-day Kattenstoet (cat parade)."]', 0, 1) )


    def test_3_db_rows_as_object(self):
        #for row in Read( DBWIKIPEDIA ).as_object( WikipediaItem ):
        for row in Read( DBWIKIPEDIA, cls=WikipediaItem ):
            self.assertIsInstance( row, WikipediaItem )
            self.assertEqual( row.PK, "en§Cat§DISAMBIGUATION_INDEF_INDEF_DOMESTICATED§0" )
            self.assertEqual( row.LabelName, "Cat" )


    def test_4(self):
        rows = Read( DBWIKIPEDIA, table="wikipedia"  )
        self.assertEqual( len(list(rows)), 1 )


    def test_5(self):
        rows = Read( DBWIKIPEDIA, table="wikipedia", where="LabelName = ? ", params=["Cat"]  )
        self.assertEqual( len(list(rows)), 1 )


    def test_11(self):
        #rows = Read( DBWIKIPEDIA, "SELECT * FROM wikipedia WHERE LabelName = ? ", "Cat"  )
        #self.assertEqual( len(list(rows)), 1 )
        ...


    def test_12a( self ):
        #rows = Read( DBWIKIPEDIA, "SELECT * FROM wikipedia WHERE LabelName = ? ", "Cat" )
        #self.assertEqual( len(list(rows)), 1 )
        ...


    def test_12b( self ):
        rows = Read( DBWIKIPEDIA, "SELECT * FROM wikipedia WHERE LabelName = ? ", params=("Cat",)  )
        self.assertEqual( len(list(rows)), 1 )


    def test_13(self):
        rows = Read( DBWIKIPEDIA, table="wikipedia", cls=WikipediaItem )
        self.assertEqual( len(list(rows)), 1 )


    def test_14(self):
        rows = Read( WikipediaItem )
        self.assertEqual( len(list(rows)), 1 )


    def test_15(self):
        rows = Read( WikipediaItem, sql="SELECT * FROM wikipedia WHERE LabelName = ? ", params=["Cat"] )
        self.assertEqual( len(list(rows)), 1 )


    def test_16(self):
        #rows = Read( DBWIKIPEDIA, "SELECT * FROM wikipedia WHERE LabelName = ? ", "Cat" )
        #self.assertEqual( len(list(rows)), 1 )
        ...


    def test_17(self):
        #for row in Read( DBWIKIPEDIA, "SELECT * FROM wikipedia WHERE LabelName = ? ", "Cat" ):
        #    self.assertEqual( row[0], "en§Cat§DISAMBIGUATION_INDEF_INDEF_DOMESTICATED§0" )
        ...


    def test_18(self):
        def convert_callack( row ):
            print( row )
            return row
        #Read( DBWIKIPEDIA ).map( convert_callack )
        #Read( DBWIKIPEDIA ).map( convert_callack ).write( DBWIKIPEDIA )



if __name__ == '__main__':
    unittest.main()
