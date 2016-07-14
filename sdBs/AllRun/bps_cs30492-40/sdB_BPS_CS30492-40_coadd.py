from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[316.897292,-38.111669],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_BPS_CS30492-40/sdB_BPS_CS30492-40_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_BPS_CS30492-40/sdB_BPS_CS30492-40_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
