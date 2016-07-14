from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[73.813417,13.091611],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_rat_j0455+1305/sdB_rat_j0455+1305_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_rat_j0455+1305/sdB_rat_j0455+1305_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
