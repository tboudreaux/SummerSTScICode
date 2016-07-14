from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[294.911708,-6.063733],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HD_185510/sdB_HD_185510_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HD_185510/sdB_HD_185510_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
