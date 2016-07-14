from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[228.4075,19.836806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_151337.80+195012.5/sdB_SDSSJ_151337.80+195012.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_151337.80+195012.5/sdB_SDSSJ_151337.80+195012.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
