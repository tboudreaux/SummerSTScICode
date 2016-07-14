from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[43.249625,-6.001792],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_02505-0612/sdB_kuv_02505-0612_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_02505-0612/sdB_kuv_02505-0612_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
