from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[203.952333,0.906389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_133548.56-005423.0/sdB_SDSSJ_133548.56-005423.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_133548.56-005423.0/sdB_SDSSJ_133548.56-005423.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
