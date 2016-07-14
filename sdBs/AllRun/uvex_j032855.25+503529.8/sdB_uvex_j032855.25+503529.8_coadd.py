from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[52.230208,50.591611],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_uvex_j032855.25+503529.8/sdB_uvex_j032855.25+503529.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_uvex_j032855.25+503529.8/sdB_uvex_j032855.25+503529.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
