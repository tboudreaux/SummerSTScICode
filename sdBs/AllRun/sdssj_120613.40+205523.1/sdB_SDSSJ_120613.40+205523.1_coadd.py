from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[181.555833,20.923083],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_120613.40+205523.1/sdB_SDSSJ_120613.40+205523.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_120613.40+205523.1/sdB_SDSSJ_120613.40+205523.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
