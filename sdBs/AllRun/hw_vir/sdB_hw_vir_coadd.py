from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[191.084208,-8.671092],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hw_vir/sdB_hw_vir_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hw_vir/sdB_hw_vir_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
