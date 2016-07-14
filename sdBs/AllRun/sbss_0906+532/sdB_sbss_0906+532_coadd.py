from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[137.419542,53.070139],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sbss_0906+532/sdB_sbss_0906+532_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sbss_0906+532/sdB_sbss_0906+532_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
