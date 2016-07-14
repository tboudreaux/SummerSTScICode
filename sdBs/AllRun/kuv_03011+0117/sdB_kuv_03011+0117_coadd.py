from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[45.928417,1.482033],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_03011+0117/sdB_kuv_03011+0117_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_03011+0117/sdB_kuv_03011+0117_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
