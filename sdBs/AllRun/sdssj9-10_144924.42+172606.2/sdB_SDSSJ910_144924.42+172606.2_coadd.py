from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[222.35175,17.435056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_144924.42+172606.2/sdB_SDSSJ910_144924.42+172606.2_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_144924.42+172606.2/sdB_SDSSJ910_144924.42+172606.2_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
