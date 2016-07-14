from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[350.230292,-5.856131],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LB_1173/sdB_LB_1173_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LB_1173/sdB_LB_1173_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
