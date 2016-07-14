from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[201.426708,-1.782056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_132542.41-014655.4/sdB_sdssj_132542.41-014655.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_132542.41-014655.4/sdB_sdssj_132542.41-014655.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
