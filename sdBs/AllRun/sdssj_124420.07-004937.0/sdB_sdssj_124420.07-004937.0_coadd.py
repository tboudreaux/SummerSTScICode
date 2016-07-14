from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[191.083625,0.826944],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_124420.07-004937.0/sdB_sdssj_124420.07-004937.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_124420.07-004937.0/sdB_sdssj_124420.07-004937.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
