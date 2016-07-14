from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[268.514917,53.693389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hs_1753+5342/sdB_hs_1753+5342_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hs_1753+5342/sdB_hs_1753+5342_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
