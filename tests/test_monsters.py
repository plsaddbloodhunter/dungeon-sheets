from unittest import TestCase

from dungeonsheets import monsters


class AutoGeneratedMonsters(TestCase):
    initializable_classes = [
        monsters.Ankylosaurus,
        monsters.Aboleth,
        monsters.Acolyte,
        monsters.AdultBlackDragon,
        monsters.AdultBlueDragon,
        monsters.AdultBrassDragon,
        monsters.AdultBronzeDragon,
        monsters.AdultCopperDragon,
        monsters.AdultGoldDragon,
        monsters.AdultGreenDragon,
        monsters.AdultRedDragon,
        monsters.AdultSilverDragon,
        monsters.AdultWhiteDragon,
        monsters.AirElemental,
        monsters.AncientBlackDragon,
        monsters.AncientBlueDragon,
        monsters.AncientBrassDragon,
        monsters.AncientBronzeDragon,
        monsters.AncientCopperDragon,
        monsters.AncientGoldDragon,
        monsters.AncientGreenDragon,
        monsters.AncientRedDragon,
        monsters.AncientSilverDragon,
        monsters.AncientWhiteDragon,
        monsters.Androsphinx,
        monsters.AnimatedArmor,
        monsters.Ankheg,
        monsters.Ape,
        monsters.Archmage,
        monsters.Assassin,
        monsters.AwakenedShrub,
        monsters.AwakenedTree,
        monsters.AxeBeak,
        monsters.Azer,
        monsters.Baboon,
        monsters.Badger,
        monsters.Balor,
        monsters.Bandit,
        monsters.BanditCaptain,
        monsters.BarbedDevil,
        monsters.Basilisk,
        monsters.Bat,
        monsters.BeardedDevil,
        monsters.Behir,
        monsters.Berserker,
        monsters.BlackBear,
        monsters.BlackDragonWyrmling,
        monsters.BlackPudding,
        monsters.BlinkDog,
        monsters.BloodHawk,
        monsters.BlueDragonWyrmling,
        monsters.Boar,
        monsters.BoneDevil,
        monsters.BrassDragonWyrmling,
        monsters.BronzeDragonWyrmling,
        monsters.BrownBear,
        monsters.Bugbear,
        monsters.Bulette,
        monsters.Camel,
        monsters.Cat,
        monsters.Centaur,
        monsters.ChainDevil,
        monsters.Chimera,
        monsters.Chuul,
        monsters.ClayGolem,
        monsters.Cloaker,
        monsters.CloudGiant,
        monsters.Cockatrice,
        monsters.Commoner,
        monsters.ConstrictorSnake,
        monsters.CopperDragonWyrmling,
        monsters.Couatl,
        monsters.Crab,
        monsters.Crocodile,
        monsters.CultFanatic,
        monsters.Cultist,
        monsters.Darkmantle,
        monsters.DeathDog,
        monsters.DeepGnomeSvirfneblin,
        monsters.Deer,
        monsters.Deva,
        monsters.DireWolf,
        monsters.Djinni,
        monsters.Doppelganger,
        monsters.DraftHorse,
        monsters.DragonTurtle,
        monsters.Dretch,
        monsters.Drider,
        monsters.Drow,
        monsters.Druid,
        monsters.Dryad,
        monsters.Duergar,
        monsters.DustMephit,
        monsters.Eagle,
        monsters.EarthElemental,
        monsters.Efreeti,
        monsters.Elephant,
        monsters.Elk,
        monsters.Erinyes,
        monsters.Ettercap,
        monsters.Ettin,
        monsters.FireElemental,
        monsters.FireGiant,
        monsters.FleshGolem,
        monsters.FlyingSnake,
        monsters.FlyingSword,
        monsters.Frog,
        monsters.FrostGiant,
        monsters.Gargoyle,
        monsters.GelatinousCube,
        monsters.Ghast,
        monsters.Ghost,
        monsters.Ghoul,
        monsters.GiantApe,
        monsters.GiantBadger,
        monsters.GiantBat,
        monsters.GiantBoar,
        monsters.GiantCentipede,
        monsters.GiantConstrictorSnake,
        monsters.GiantCrab,
        monsters.GiantCrocodile,
        monsters.GiantEagle,
        monsters.GiantElk,
        monsters.GiantFireBeetle,
        monsters.GiantFrog,
        monsters.GiantGoat,
        monsters.GiantHyena,
        monsters.GiantLizard,
        monsters.GiantOctopus,
        monsters.GiantOwl,
        monsters.GiantPoisonousSnake,
        monsters.GiantRat,
        monsters.GiantRatDiseased,
        monsters.GiantScorpion,
        monsters.GiantSeaHorse,
        monsters.GiantShark,
        monsters.GiantSpider,
        monsters.GiantToad,
        monsters.GiantVulture,
        monsters.GiantWasp,
        monsters.GiantWeasel,
        monsters.GiantWolfSpider,
        monsters.GibberingMouther,
        monsters.Glabrezu,
        monsters.Gladiator,
        monsters.Gnoll,
        monsters.Goat,
        monsters.Goblin,
        monsters.GoldDragonWyrmling,
        monsters.Gorgon,
        monsters.GrayOoze,
        monsters.GreenDragonWyrmling,
        monsters.GreenHag,
        monsters.Grick,
        monsters.Griffon,
        monsters.Grimlock,
        monsters.Guard,
        monsters.GuardianNaga,
        monsters.Gynosphinx,
        monsters.HalfRedDragonVeteran,
        monsters.Harpy,
        monsters.Hawk,
        monsters.HellHound,
        monsters.Hezrou,
        monsters.HillGiant,
        monsters.Hippogriff,
        monsters.Hobgoblin,
        monsters.Homunculus,
        monsters.HornedDevil,
        monsters.HunterShark,
        monsters.Hydra,
        monsters.Hyena,
        monsters.IceDevil,
        monsters.IceMephit,
        monsters.Imp,
        monsters.InvisibleStalker,
        monsters.IronGolem,
        monsters.Jackal,
        monsters.KillerWhale,
        monsters.Knight,
        monsters.Kobold,
        monsters.Kraken,
        monsters.Lamia,
        monsters.Lemure,
        monsters.Lich,
        monsters.Lion,
        monsters.Lizard,
        monsters.Lizardfolk,
        monsters.Mage,
        monsters.MagmaMephit,
        monsters.Magmin,
        monsters.Mammoth,
        monsters.Manticore,
        monsters.Marilith,
        monsters.Mastiff,
        monsters.Medusa,
        monsters.Merfolk,
        monsters.Merrow,
        monsters.Mimic,
        monsters.Minotaur,
        monsters.MinotaurSkeleton,
        monsters.Mule,
        monsters.Mummy,
        monsters.MummyLord,
        monsters.Nalfeshnee,
        monsters.NightHag,
        monsters.Nightmare,
        monsters.Noble,
        monsters.OchreJelly,
        monsters.Octopus,
        monsters.Ogre,
        monsters.OgreZombie,
        monsters.Oni,
        monsters.Orc,
        monsters.Otyugh,
        monsters.Owl,
        monsters.Owlbear,
        monsters.Panther,
        monsters.Pegasus,
        monsters.PhaseSpider,
        monsters.PitFiend,
        monsters.Planetar,
        monsters.Plesiosaurus,
        monsters.PoisonousSnake,
        monsters.PolarBear,
        monsters.Pony,
        monsters.Priest,
        monsters.Pseudodragon,
        monsters.PurpleWorm,
        monsters.Quasit,
        monsters.Quipper,
        monsters.Rakshasa,
        monsters.Rat,
        monsters.Raven,
        monsters.RedDragonWyrmling,
        monsters.ReefShark,
        monsters.Remorhaz,
        monsters.Rhinoceros,
        monsters.RidingHorse,
        monsters.Roc,
        monsters.Roper,
        monsters.RugofSmothering,
        monsters.RustMonster,
        monsters.SaberToothedTiger,
        monsters.Sahuagin,
        monsters.Salamander,
        monsters.Satyr,
        monsters.Scorpion,
        monsters.Scout,
        monsters.SeaHag,
        monsters.SeaHorse,
        monsters.Shadow,
        monsters.ShamblingMound,
        monsters.ShieldGuardian,
        monsters.Shrieker,
        monsters.SilverDragonWyrmling,
        monsters.Skeleton,
        monsters.Solar,
        monsters.Specter,
        monsters.Spider,
        monsters.SpiritNaga,
        monsters.Sprite,
        monsters.Spy,
        monsters.SteamMephit,
        monsters.Stirge,
        monsters.StoneGiant,
        monsters.StoneGolem,
        monsters.StormGiant,
        monsters.SuccubusIncubus,
        monsters.SwarmofBats,
        monsters.SwarmofBeetles,
        monsters.SwarmofCentipedes,
        monsters.SwarmofInsects,
        monsters.SwarmofPoisonousSnakes,
        monsters.SwarmofQuippers,
        monsters.SwarmofRats,
        monsters.SwarmofRavens,
        monsters.SwarmofSpiders,
        monsters.SwarmofWasps,
        monsters.Tarrasque,
        monsters.Thug,
        monsters.Tiger,
        monsters.Treant,
        monsters.TribalWarrior,
        monsters.Triceratops,
        monsters.Troll,
        monsters.TyrannosaurusRex,
        monsters.Unicorn,
        monsters.Vampire,
        monsters.VampireSpawn,
        monsters.Veteran,
        monsters.VioletFungus,
        monsters.Vrock,
        monsters.Vulture,
        monsters.Warhorse,
        monsters.WarhorseSkeleton,
        monsters.WaterElemental,
        monsters.Weasel,
        monsters.WerebearBearform,
        monsters.WerebearHumanform,
        monsters.WerebearHybridform,
        monsters.WereboarBoarform,
        monsters.WereboarHumanform,
        monsters.WereboarHybridform,
        monsters.WereratHumanform,
        monsters.WereratHybridform,
        monsters.WereratRatform,
        monsters.WeretigerHumanform,
        monsters.WeretigerHybridform,
        monsters.WeretigerTigerform,
        monsters.WerewolfHumanform,
        monsters.WerewolfHybridform,
        monsters.WerewolfWolfform,
        monsters.WhiteDragonWyrmling,
        monsters.Wight,
        monsters.WilloWisp,
        monsters.WinterWolf,
        monsters.Wolf,
        monsters.Worg,
        monsters.Wraith,
        monsters.Wyvern,
        monsters.Xorn,
        monsters.YoungBlackDragon,
        monsters.YoungBlueDragon,
        monsters.YoungBrassDragon,
        monsters.YoungBronzeDragon,
        monsters.YoungCopperDragon,
        monsters.YoungGoldDragon,
        monsters.YoungGreenDragon,
        monsters.YoungRedDragon,
        monsters.YoungSilverDragon,
        monsters.YoungWhiteDragon,
        monsters.Zombie
    ]

    def test_createable(self):
        for InitializableClass in self.initializable_classes:
            # All classes should be initializable, so just try to
            # create each monster
            _ = InitializableClass()

    def test_ability_scores(self):
        wolf = monsters.Wolf()
        self.assertEqual(wolf.strength.value, 12)
        self.assertEqual(wolf.strength.modifier, 1)
        self.assertEqual(wolf.strength.saving_throw, 1)
