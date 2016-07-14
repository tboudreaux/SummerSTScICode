from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[337.073583,-7.996639],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_222817.66-075947.9/sdB_sdssj_222817.66-075947.9_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_222817.66-075947.9/sdB_sdssj_222817.66-075947.9_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
