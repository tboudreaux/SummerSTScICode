from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[138.67812,-10.825333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_003658.85-104931.2/sdB_SDSSJ_003658.85-104931.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_003658.85-104931.2/sdB_SDSSJ_003658.85-104931.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
