from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[122.706125,74.966056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_bd_+75325/sdB_bd_+75325_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_bd_+75325/sdB_bd_+75325_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
