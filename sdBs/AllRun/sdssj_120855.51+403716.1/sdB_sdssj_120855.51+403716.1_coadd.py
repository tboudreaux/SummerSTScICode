from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[182.231292,40.621139],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_120855.51+403716.1/sdB_sdssj_120855.51+403716.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_120855.51+403716.1/sdB_sdssj_120855.51+403716.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
