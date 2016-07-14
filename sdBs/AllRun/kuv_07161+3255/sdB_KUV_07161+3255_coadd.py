from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[109.837917,32.820156],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_07161+3255/sdB_KUV_07161+3255_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_07161+3255/sdB_KUV_07161+3255_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()