from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[45.490042,1.533467],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_02594+0120/sdB_kuv_02594+0120_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_02594+0120/sdB_kuv_02594+0120_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
