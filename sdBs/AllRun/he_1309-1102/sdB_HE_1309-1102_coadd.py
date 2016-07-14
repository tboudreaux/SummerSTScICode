from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[198.009917,-11.304528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HE_1309-1102/sdB_HE_1309-1102_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HE_1309-1102/sdB_HE_1309-1102_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
