import json
import sys
from Utils.Config import Config
from Utils.Fingerprint import Fingerprint
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards

class Players:

	try:
		config = open('config.json', 'r')
		content = config.read()
	except FileNotFoundError:
		print("Creating config.json...")
		Config.create_config()
		config = open('config.json', 'r')
		content = config.read()

	settings = json.loads(content)

	
	HighID = 0
	LowID = 0
	Token = None
	boxID = 0
	mapID = 7
	roomID = 0
	brawlerID = 0
	skinID = 0


	SkinsCount = Skins.get_skins_id()
	BrawlersCount = Characters.get_brawlers_id()
	CardSkillsID = Cards.get_spg_id()
	CardUnlockID = Cards.get_brawler_unlock()


	brawler_power_level = settings['BrawlerPowerLevel']
	brawler_trophies_for_rank = settings['BrawlerTrophiesForRank']
	brawler_trophies = settings['BrawlerTrophies']
	brawler_upgrade_points = settings['BrawlerUpgradePoints']
	trophies = settings['Trophies']
	gems = settings['Gems']
	gold = settings['Gold']
	tickets = settings['Tickets']
	name = None
	profileIcon = 0
	brawlBoxes = settings['BrawlBoxTokens']
	bigBoxes = settings['BigBoxTokens']
	starPoints = settings['Starpoints']


	Resources = {
		'brawlbox': {'id': 1, 'amount': brawlBoxes},
		'gold': {'id': 8, 'amount': gold},
		'bigbox': {'id': 9, 'amount':bigBoxes},
		'starpoints': {'id': 10, 'amount': starPoints}
	}


	updateUrl = settings['UpdateUrl']
	patchUrl = settings['PatchUrl']
	patch_sha = Fingerprint.loadFinger("GameAssets/fingerprint.json")

	err_code = 7
	maintenance = False
	patch = False

	patching = settings['Patch']

	if patching:
		error_code = 7
		patch = True


	if settings['Maintenance']:
		err_code = 10
		maintenance = True

	messageTick = 0
	botMessageTick = 0

	shellySkin = 0
	nitaSkin = 0
	coltSkin = 0
	bullSkin = 0
	jessieSkin = 0
	brockSkin = 0
	dynamikeSkin = 0
	boSkin = 0
	elprimoSkin = 0
	barleySkin = 0
	pocoSkin = 0
	ricoSkin = 0
	darrylSkin = 0
	pennySkin = 0
	piperSkin = 0
	pamSkin = 0
	frankSkin = 0
	mortisSkin = 0
	taraSkin = 0
	spikeSkin = 0
	crowSkin = 0
	geneSkin = 0
	tickSkin = 0
	leonSkin = 0
	rosaSkin = 0
	carlSkin = 0
	bibiSkin = 0
	bitSkin = 0
	sandySkin =0
	beaSkin = 0
	emzSkin = 0
	mrpSkin = 0
	maxSkin = 0
	jackySkin =0
	galeSkin = 0
	naniSkin = 0
	sproutSkin =0
	gadget = 255
	starpower = 76
	namecolor = 12
	GameType = 0
	Rank = 0
	Team = 0
	Bot1 = 0
	Bot1N = None
	Bot2 = 0
	Bot2N = None
	Bot3 = 0
	Bot3N = None
	Bot4 = 0
	Bot4N = None
	Bot5 = 0
	Bot5N = None
	useGadget = 1
	DoNotDistrub = 0


	def __init__(self, device):
		self.device = device