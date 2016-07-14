from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[268.337167,70.426142],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HS_1753+7025/sdB_HS_1753+7025_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HS_1753+7025/sdB_HS_1753+7025_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
